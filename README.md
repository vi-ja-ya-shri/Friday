# Friday – Voice & Video AI Assistant

Friday is a real-time **voice and video AI assistant** built with the **LiveKit Agents SDK** and **Google Gemini Realtime API**.  
It can **listen, speak, and interact over video** while adopting the witty persona of a classy butler inspired by Iron Man.  
Friday doesn’t just chat – it can also **fetch weather updates, search the web, and send emails** through built-in tools.

---

## 🚀 Features
- **Real-Time Voice Interaction**: Low-latency speech-to-text & text-to-speech with Google Gemini.
- **Video Support**: Join video calls with users, powered by LiveKit.
- **Custom Persona**: “Friday” – a sarcastic butler personality defined by prompts.
- **Noise Cancellation**: Clean audio input using LiveKit’s BVC plugin.
- **Integrated Tools**:
  - 🌤️ **Weather Tool** – Get current city weather via [wttr.in](https://wttr.in).
  - 🔎 **Web Search Tool** – Search the web using DuckDuckGo.
  - 📧 **Email Tool** – Send emails via Gmail SMTP.

---


## 📂 Project Structure
├── agent.py # Main entrypoint – sets up assistant session with LiveKit
├── prompts.py # Defines persona (AGENT_INSTRUCTION) & greeting (SESSION_INSTRUCTION)
├── tools.py # External tools (weather, web search, email)
└── .env # Environment variables (not checked into repo)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/friday-assistant.git
cd friday-assistant

