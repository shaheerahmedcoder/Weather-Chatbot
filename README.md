# 🌦️ Weather Chatbot

An **AI powered Weather Chatbot** that provides real-time weather information in a conversational way. The chatbot fetches live weather data using the **OpenWeather API** and generates human-like, context-aware responses using **Google Gemini**. The application is built with **Python** and **Streamlit** for a clean and interactive UI.

---

## 🚀 Features

* 🌍 Real-time weather updates for any city
* 🤖 AI-generated natural language responses
* ☁️ Powered by OpenWeather API
* 🧠 Uses Google Gemini for intelligent replies
* 🎨 Simple and interactive Streamlit interface
* 🔐 Secure API key management using environment variables

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** – frontend UI
* **OpenWeather API** – live weather data
* **Google Gemini API** – AI-powered responses
* **Requests** – API handling
* **python-dotenv** – environment variable management

---

## 📂 Project Structure

```text
Weather-Chatbot/
│
├── app.py                # Core chatbot logic
├── streamlit_app.py      # Streamlit UI entry point
├── requirements.txt      # Project dependencies
├── .env.example          # Sample environment variables
├── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shaheerahmedcoder/Weather-Chatbot.git
cd Weather-Chatbot
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
GEMINI_API_KEY=your_gemini_api_key
```

> ⚠️ Never commit your `.env` file to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run streamlit_app.py
```

The app will open automatically in your browser.

---

## 💡 How It Works

1. User enters a city name or weather-related query.
2. The app fetches live weather data from OpenWeather API.
3. Weather data is passed to Google Gemini.
4. Gemini generates a natural, conversational response.
5. The response is displayed in the Streamlit UI.

---

## 🧪 Example Use Cases

* "What’s the weather in Lahore today?"
* "Is it a good day to go outside in Karachi?"
* "Tell me tomorrow’s weather in Islamabad"

---

## 📸 Screenshots 

<img width="1920" height="642" alt="image" src="https://github.com/user-attachments/assets/2ef09168-3504-45dd-be65-d878197e67ed" />


---

## 🔐 API References

* OpenWeather API – Weather data
* Google Gemini API – AI-generated responses

---

## 🧠 Learning Outcomes

* API integration in Python
* Secure API key handling
* Streamlit-based UI development
* Practical use of Generative AI (Gemini)
* Prompt engineering for contextual responses

---

## 🚧 Future Improvements

* 🌤️ 7-day weather forecast
* 📍 Auto-detect location
* 🌐 Multi-language support
* 📱 Mobile-friendly UI
* 🧠 Memory-based conversations

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes
4. Open a Pull Request

---

## 👤 Author

**Shaheer Ahmed**
Full Stack Developer | Generative AI Enthusiast

* GitHub: [https://github.com/shaheerahmedcoder](https://github.com/shaheerahmedcoder)

---

⭐ If you found this project useful, consider giving it a star!
