#!/bin/bash

# This script starts the backend on Unix systems (macOS/Linux)

echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Starting backend on port 5000..."
echo "Open another terminal and run: cd frontend && python -m http.server 3000"
echo ""

cd backend
python app.py
