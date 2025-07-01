from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.gpt_handler import get_ayatori_response
from app.elevenlabs_handler import speak_response
from app.memory import log_interaction
import os

app = FastAPI()

VOICE_ID = os.getenv("VOICE_ID")

class TranscriptionPayload(BaseModel):
    text: str
    participant: str = "unknown"

@app.post("/webhook")
async def handle_webhook(payload: TranscriptionPayload):
    user_text = payload.text
    participant = payload.participant

    response_text = get_ayatori_response(user_text, participant)
    log_interaction(participant, user_text, response_text)
    speak_response(response_text, VOICE_ID)

    return {"status": "ok", "response": response_text}
