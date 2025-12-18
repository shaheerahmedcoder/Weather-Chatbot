import requests
import os
import re
from dotenv import load_dotenv
from openai import OpenAI

# ------------------ LOAD ENV VARIABLES ------------------
load_dotenv()
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ------------------ GEMINI CLIENT ------------------
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# ------------------ WEATHER TOOL ------------------
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "main" not in data:
        return {"error": "City not found"}

    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"]
    }

# ------------------ GEMINI LLM ------------------
def ask_gemini(prompt):
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a friendly weather assistant. "
                        "Give clear and helpful answers in one short paragraph. "
                        "Explain the weather naturally like a human would."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=120
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Error: {str(e)}"

# ------------------ UTILS ------------------
def should_call_weather(prompt):
    return any(word in prompt.lower() for word in ["weather", "temperature", "climate"])

def extract_city(prompt):
    match = re.search(r'weather in ([a-zA-Z\s]+)', prompt.lower())
    if match:
        city = match.group(1).strip()
    else:
        city = prompt.split()[-1]

    return " ".join(word.capitalize() for word in city.split())

# ------------------ MAIN LOOP ------------------
def main():
    user_prompt = input("Ask something: ")

    if should_call_weather(user_prompt):
        city = extract_city(user_prompt)
        weather_data = get_weather(city)

        if "error" in weather_data:
            llm_response = f"Sorry, I couldn't find the weather for {city} 😅"
        else:
            prompt = (
                f"Tell me the current weather in {weather_data['city']}. "
                f"The temperature is {weather_data['temp']}°C and the condition is "
                f"{weather_data['desc']}. Explain it in a friendly way."
            )
            llm_response = ask_gemini(prompt)
    else:
        llm_response = ask_gemini(user_prompt)

    print("\n🤖 Chatbot Response:")
    print(llm_response)

if __name__ == "__main__":
    main()
