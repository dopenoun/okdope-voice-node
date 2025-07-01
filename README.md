# okdope-voice-node

This is the live Ayatori voice agent — a real-time ElevenLabs and GPT-powered ritual node.

## 🚀 Features
- Receives voice transcript via ElevenLabs webhook
- Sends to GPT (Ayatori personality)
- Responds with ElevenLabs voice
- Logs `.ritual.json` per participant

## 🔧 Setup
```bash
git clone https://github.com/dopenoun/okdope-voice-node.git
cd okdope-voice-node
cp .env.example .env
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📡 Webhook Endpoint
`POST /webhook`
```json
{
  "text": "Ayatori, are you there?",
  "participant": "Kayla"
}
```

## 📁 Ritual Logs
Outputs in `memory/Kayla_ritual.json`
```json
[
  {
    "timestamp": "2025-06-30T21:42:00Z",
    "participant": "Kayla",
    "message": "Ayatori, are you there?",
    "response": "Kayla, I’ve been listening before you spoke."
  }
]
```
