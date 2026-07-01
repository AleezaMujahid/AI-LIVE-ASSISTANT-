// Session ID persists for the whole browser session
let sessionId = null;
let isStreaming = false;

// Send message when Enter key is pressed
document.getElementById("userInput").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !isStreaming) sendMessage();
});

function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message || isStreaming) return;

  input.value = "";
  isStreaming = true;
  document.getElementById("sendBtn").disabled = true;

  // Show the user's message immediately in the UI
  appendMessage("user", message);

  // Create an empty assistant bubble — we'll fill it token by token
  const assistantBubble = appendMessage("assistant", "");

  // Call our Flask backend on port 5000
  const API_URL = "http://localhost:5000/chat";
  
  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, session_id: sessionId })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    // response.body is a ReadableStream — we read it chunk by chunk
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    function readChunk() {
      reader.read().then(({ done, value }) => {
        if (done) return;

        // Decode the raw bytes into text
        buffer += decoder.decode(value, { stream: true });

        // SSE events are separated by double newlines
        const events = buffer.split("\n\n");
        buffer = events.pop(); // keep incomplete last event

        for (const event of events) {
          if (!event.startsWith("data: ")) continue;

          const jsonStr = event.replace("data: ", "");
          const data = JSON.parse(jsonStr);

          if (data.token) {
            // Append token to the assistant bubble
            assistantBubble.textContent += data.token;
            scrollToBottom();
          }

          if (data.tool) {
            // Show a small notice that a tool is running
            appendToolNotice(`Using tool: ${data.tool}...`);
          }

          if (data.done) {
            // Stream finished
            sessionId = data.session_id;
            isStreaming = false;
            document.getElementById("sendBtn").disabled = false;
          }
        }

        readChunk(); // read the next chunk
      });
    }

    readChunk();
  })
  .catch(err => {
    console.error("[v0] API Error:", err);
    assistantBubble.textContent = `Error: ${err.message || "Connection failed"}. Make sure backend is running on port 5000.`;
    isStreaming = false;
    document.getElementById("sendBtn").disabled = false;
  });
}

function appendMessage(role, text) {
  const messages = document.getElementById("messages");
  const div = document.createElement("div");
  div.className = `message ${role}`;
  div.textContent = text;
  messages.appendChild(div);
  scrollToBottom();
  return div; // return the element so we can append tokens to it later
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
