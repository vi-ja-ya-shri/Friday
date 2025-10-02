
# Friday – Voice & Video AI Assistant

Friday is a real-time **voice and video AI assistant** built with the **LiveKit Agents SDK** and **Google Gemini Realtime API**.
It can **listen, speak, and interact over video** while adopting the witty persona of a classy butler inspired by Iron Man.
Friday doesn’t just chat – it can also **fetch weather updates, search the web, and send emails** through built-in tools.

---

## 🚀 Features

* **Real-Time Voice Interaction**: Low-latency speech-to-text & text-to-speech with Google Gemini.
* **Video Support**: Join video calls with users, powered by LiveKit.
* **Custom Persona**: “Friday” – a sarcastic butler personality defined by prompts.
* **Noise Cancellation**: Clean audio input using LiveKit’s BVC plugin.
* **Integrated Tools**:

  * 🌤️ **Weather Tool** – Get current city weather via [wttr.in](https://wttr.in).
  * 🔎 **Web Search Tool** – Search the web using DuckDuckGo.
  * 📧 **Email Tool** – Send emails via Gmail SMTP.

---

## 📂 Project Structure

```
├── agent.py        # Main entrypoint – sets up assistant session with LiveKit
├── prompts.py      # Defines persona (AGENT_INSTRUCTION) & greeting (SESSION_INSTRUCTION)
├── tools.py        # External tools (weather, web search, email)
└── .env            # Environment variables (not checked into repo)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/friday-assistant.git
cd friday-assistant
```

### 2. Python Environment

Use Python **3.9+**. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install livekit-agents livekit-plugins-google livekit-plugins-noise-cancellation python-dotenv requests langchain-community
```

### 4. Environment Variables

Create a `.env` file in the project root:

```env
# LiveKit credentials
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret

# Google Gemini API key
GOOGLE_API_KEY=your_google_api_key

# Gmail credentials for email tool
GMAIL_USER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password
```

---

## ▶️ Running the Assistant

Run the worker with:

```bash
python agent.py
```

This starts the LiveKit agent worker.
Join the same room (via LiveKit Playground or your client app) and Friday will greet you:

> “Hi my name is Friday, your personal assistant, how may I help you?”

---

## 📝 Usage Examples

* **Weather**:
  User: *“What’s the weather in London?”*
  Friday: *“Certainly, sir. London: 🌤️ 15°C.”*

* **Web Search**:
  User: *“Search for today’s tech news.”*
  Friday: *“Check! Here are some top tech news results: …”*

* **Send Email**:
  User: *“Send an email to [alice@example.com](mailto:alice@example.com) with subject Meeting and message I’ll call at 5.”*
  Friday: *“Will do, ma’am. ✅ Email sent successfully to [alice@example.com](mailto:alice@example.com).”*

---

## 🛠️ Tech Stack

* **[LiveKit Agents SDK](https://github.com/livekit/agents)** – Real-time voice & video streaming.
* **Google Gemini Realtime API** – Conversational LLM with speech support.
* **WTTR.in API** – Weather data source.
* **DuckDuckGo (LangChain)** – Web search tool.
* **Gmail SMTP** – Email sending.
* **Python (asyncio)** – Asynchronous event handling.

---

## 📌 Known Issues

* Requires valid **API keys** for LiveKit, Gemini, and Gmail.
* Video input is enabled but not yet analyzed by AI (future enhancement).
* Responses limited to **one sentence** due to persona instructions.

---

## 🤝 Contribution

1. Fork this repo
2. Create a feature branch
3. Commit changes
4. Open a Pull Request 🚀

---
