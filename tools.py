import requests
import os

def get_weather(city: str) -> str:
    """Get current weather for a city using wttr.in (free, no API key needed)"""
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=5
        )
        if response.status_code == 200:
            return response.text.strip()
        return f"Could not fetch weather for {city}"
    except Exception as e:
        return f"Weather tool error: {str(e)}"


def calculate(expression: str) -> str:
    """Safely evaluate a math expression"""
    try:
        # Only allow safe characters — no imports, no exec
        allowed = set("0123456789+-*/()., ")
        if not all(c in allowed for c in expression):
            return "Invalid expression — only numbers and operators allowed"
        result = eval(expression)
        return f"{expression} = {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"


def search_web(query: str) -> str:
    """Search using DuckDuckGo instant answers (free, no API key)"""
    try:
        response = requests.get(
            "https://api.duckduckgo.com/",
            params={"q": query, "format": "json", "no_html": 1},
            timeout=5
        )
        data = response.json()
        answer = data.get("AbstractText") or data.get("Answer") or ""
        if answer:
            return answer[:500]
        return f"No instant answer found for: {query}"
    except Exception as e:
        return f"Search error: {str(e)}"