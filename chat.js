let sessionId = null;
let isStreaming = false;

document.getElementById("userInput").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !isStreaming) sendMessage();
});

async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message || isStreaming) return;

  input.value = "";
  isStreaming = true;
  document.getElementById("sendBtn").disabled = true;

  appendMessage("user", message);
  const assistantBubble = appendMessage("assistant", "");

  try {
    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: message, session_id: sessionId })
    });

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const events = buffer.split("\n\n");
      buffer = events.pop();

      for (const event of events) {
        if (!event.startsWith("data: ")) continue;

        try {
          const jsonStr = event.slice(6); // removes "data: "
          const data = JSON.parse(jsonStr);

          if (data.token) {
            assistantBubble.textContent += data.token;
            scrollToBottom();
          }

          if (data.tool) {
            appendToolNotice(`Using tool: ${data.tool}...`);
          }

          if (data.done) {
            sessionId = data.session_id;
            isStreaming = false;
            document.getElementById("sendBtn").disabled = false;
          }

        } catch (parseErr) {
          console.error("Parse error:", parseErr, "Raw event:", event);
        }
      }
    }

  } catch (err) {
    console.error("Fetch error:", err);
    assistantBubble.textContent = `Error: ${err.message}. Make sure backend is running on port 5000.`;
    isStreaming = false;
    document.getElementById("sendBtn").disabled = false;
  }
}

function appendMessage(role, text) {
  const messages = document.getElementById("messages");
  const div = document.createElement("div");
  div.className = `message ${role}`;
  div.textContent = text;
  messages.appendChild(div);
  scrollToBottom();
  return div;
}

function appendToolNotice(text) {
  const messages = document.getElementById("messages");
  const div = document.createElement("div");
  div.className = "tool-notice";
  div.textContent = text;
  messages.appendChild(div);
}

function scrollToBottom() {
  const messages = document.getElementById("messages");
  messages.scrollTop = messages.scrollHeight;
} 