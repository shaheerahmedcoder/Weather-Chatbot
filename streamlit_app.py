import streamlit as st
from app import get_weather, ask_gemini, should_call_weather, extract_city

st.set_page_config(
    page_title="Weather Chatbot 🌤️",
    page_icon="⛅",
    layout="centered"
)

st.title("🌤️ Weather Chatbot")
st.caption("Ask real-time weather for any city worldwide")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask about weather (e.g. weather in Karachi)")

if user_input:
    st.session_state.messages.append(("You", user_input))

    if should_call_weather(user_input):
        city = extract_city(user_input)

        if not city:
            reply = "Please specify a city name 🌍"
        else:
            weather = get_weather(city)
            if not weather:
                reply = f"Sorry, I couldn't find weather for **{city}** 😅"
            else:
                reply = ask_gemini(weather)
    else:
        reply = "I currently support weather-related questions only 🌤️"

    st.session_state.messages.append(("Bot", reply))

for role, msg in st.session_state.messages:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
