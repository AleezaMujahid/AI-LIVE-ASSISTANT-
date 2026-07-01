import json
import os
import uuid
from flask import Flask, request, Response, stream_with_context, make_response
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

from database import init_db, save_message, get_messages
from system_prompt import SYSTEM_PROMPT
from tool_dispatcher import TOOL_DEFINITIONS, run_tool

load_dotenv()

app = Flask(__name__)
CORS(app, origins="*")

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
init_db() 

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return response, 200

    data = request.get_json()
    user_message = data.get("message", "").strip()
    session_id = data.get("session_id") or str(uuid.uuid4()) 

    if not user_message:
        return {"error": "empty message"}, 400

    save_message(session_id, "user", user_message)

    history = get_messages(session_id, limit=20)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    def generate():
        full_response = ""
        tool_call_buffer = {}

        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOL_DEFINITIONS,
            tool_choice="auto",
            stream=True
        )

        for chunk in stream:
            delta = chunk.choices[0].delta

            if delta.content:
                full_response += delta.content
                yield f"data: {json.dumps({'token': delta.content})}\n\n"

            elif delta.tool_calls:
                for tc in delta.tool_calls:
                    idx = tc.index
                    if idx not in tool_call_buffer:
                        tool_call_buffer[idx] = {"name": "", "arguments": ""}
                    if tc.function.name:
                        tool_call_buffer[idx]["name"] += tc.function.name
                    if tc.function.arguments:
                        tool_call_buffer[idx]["arguments"] += tc.function.arguments

        if tool_call_buffer:
            for idx, tc in tool_call_buffer.items():
                tool_name = tc["name"]
                tool_args = json.loads(tc["arguments"])

                yield f"data: {json.dumps({'tool': tool_name})}\n\n"

                tool_result = run_tool(tool_name, tool_args)

                messages.append({
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [{
                        "id": f"call_{idx}",
                        "type": "function",
                        "function": {
                            "name": tool_name,
                            "arguments": json.dumps(tool_args)
                        }
                    }]
                })
                messages.append({
                    "role": "tool",
                    "tool_call_id": f"call_{idx}",
                    "content": tool_result
                })

            second_stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                stream=True
            )
            for chunk in second_stream:
                delta = chunk.choices[0].delta
                if delta.content:
                    full_response += delta.content
                    yield f"data: {json.dumps({'token': delta.content})}\n\n"

        if full_response:
            save_message(session_id, "assistant", full_response)

        yield f"data: {json.dumps({'done': True, 'session_id': session_id})}\n\n"

    return Response(
    stream_with_context(generate()),
    mimetype="text/event-stream",
    headers={
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",
        "Access-Control-Allow-Origin": "*"
    }
) 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)

 