@echo off
REM This script starts both the backend and frontend on Windows

echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Starting backend on port 5000...
echo Open another terminal and run: cd frontend && python -m http.server 3000
echo.

cd backend
python app.py
