import requests
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

# ------------------ LOAD ENV ------------------
load_dotenv()
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ------------------ GEMINI CLIENT ------------------
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ------------------ WEATHER API ------------------
def get_weather(city: str):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )
    response = requests.get(url, timeout=10)
    data = response.json()

    if response.status_code != 200 or "main" not in data:
        return None

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }

# ------------------ GEMINI FORMATTER ------------------
def ask_gemini(weather):
    prompt = f"""
You are a weather assistant.
DO NOT greet.
DO NOT invent information.
ONLY describe the given data naturally.

City: {weather['city']}
Country: {weather['country']}
Temperature: {weather['temperature']}°C
Feels like: {weather['feels_like']}°C
Humidity: {weather['humidity']}%
Condition: {weather['description']}
"""

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You strictly explain weather data. No greetings. No guessing."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=120
    )

    return response.choices[0].message.content.strip()

# ------------------ HELPERS ------------------
def should_call_weather(text: str) -> bool:
    keywords = ["weather", "temperature", "temp", "climate"]
    return any(k in text.lower() for k in keywords)

def extract_city(text: str) -> str | None:
    patterns = [
        r"weather in ([a-zA-Z\s]+)",
        r"weather of ([a-zA-Z\s]+)",
        r"temperature in ([a-zA-Z\s]+)",
        r"in ([a-zA-Z\s]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return match.group(1).strip().title()

    words = text.split()
    return words[-1].title() if len(words) <= 3 else None

# ------------------ CLI TEST ------------------
def main():
    user_input = input("Ask something: ")

    if should_call_weather(user_input):
        city = extract_city(user_input)

        if not city:
            print("🤖 Please mention a city name.")
            return

        weather = get_weather(city)

        if not weather:
            print(f"🤖 Sorry, I couldn't find weather for {city}.")
            return

        print("\n🤖 Chatbot Response:")
        print(ask_gemini(weather))
    else:
        print("🤖 I can help with weather only 🌤️")

if __name__ == "__main__":
    main()
