# Aria - AI Assistant

A real-time chat interface powered by GPT-4 with CORS properly configured and frontend/backend separated.

## Project Structure

```
project-root/
├── backend/              # Flask backend
│   ├── app.py           # Main Flask application
│   ├── database.py       # SQLite database functions
│   ├── tool_dispatcher.py # Tool execution logic
│   ├── tools.py         # Available tools
│   ├── system_prompt.py # AI system prompt
│   └── conversations.db # SQLite database (auto-created)
├── frontend/            # Frontend files
│   ├── index.html       # Main HTML file
│   ├── chat.js          # Chat logic and API calls
│   └── style.css        # Styling
├── .env                 # Environment variables (API keys)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Navigate to project root
cd your-project-name

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

### 4. Run Backend (Terminal 1)

```bash
cd backend
python app.py
```

You should see:
```
Running on http://0.0.0.0:5000
```

### 5. Run Frontend (Terminal 2)

Choose one method:

**Option A - Python HTTP Server:**
```bash
cd frontend
python -m http.server 3000
```

**Option B - Node.js HTTP Server:**
```bash
cd frontend
npx http-server -p 3000
```

**Option C - VS Code Live Server Extension:**
- Install "Live Server" extension
- Right-click `frontend/index.html` → "Open with Live Server"

### 6. Access the App

Open your browser and go to: `http://localhost:3000`

## CORS Configuration

- **Frontend runs on:** `http://localhost:3000`
- **Backend runs on:** `http://localhost:5000`
- **CORS is enabled** to allow cross-origin requests
- API URL in `chat.js` is set to: `http://localhost:5000/chat`

## Troubleshooting

### CORS Error
If you see a CORS error in the browser:
1. Ensure backend is running on port 5000
2. Frontend is accessing `http://localhost:5000/chat` (not port 3000)
3. Check browser console (F12) for error details

### Connection Refused
If you get "connection refused":
1. Make sure backend is running (`python backend/app.py`)
2. Backend should be on port 5000
3. Check for firewall issues

### API Key Error
- Verify `.env` file exists in project root
- Ensure `OPENAI_API_KEY` is set correctly
- Restart backend after changing `.env`

## Deactivate Virtual Environment

When done working:
```bash
deactivate
```

## Notes

- The session ID persists across messages in the same browser session
- Messages are stored in SQLite database (`conversations.db`)
- The AI can use tools/functions defined in `tool_dispatcher.py`
