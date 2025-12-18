import streamlit as st
from app import get_weather, ask_gemini, should_call_weather, extract_city

st.set_page_config(
    page_title="Weather Chatbot 🌤️",
    page_icon="⛅",
    layout="wide"
)

st.title("🌤️ Weather Chatbot")
st.markdown("Ask about the weather in any city or just chat with me!")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if should_call_weather(user_input):
        city = extract_city(user_input)
        weather_data = get_weather(city)

        if "error" in weather_data:
            bot_reply = f"Sorry, I couldn't find the weather for {city} 😅"
        else:
            prompt = (
                f"Describe today's weather in {weather_data['city']}. "
                f"The temperature is {weather_data['temp']}°C with "
                f"{weather_data['desc']}. Respond in a friendly paragraph."
            )
            bot_reply = ask_gemini(prompt)
    else:
        bot_reply = ask_gemini(user_input)

    st.session_state.messages.append({"role": "bot", "content": bot_reply})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
