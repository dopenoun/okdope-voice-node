import subprocess
import json
import os
from app.gpt_handler import get_gpt_response
from app.elevenlabs_handler import speak_text
from app.memory import save_to_memory

# 🔓 Unlock the vault from envdrop
subprocess.run(["python3", "envdrop.py", "unlock"], cwd="../envdrop")

# 🧠 Load the ritual configuration
with open(".ritual.json", "r") as f:
    ritual = json.load(f)

print(f"🔮 Ritual '{ritual['name']}' invoked: {ritual['invocation_phrase']}")

# 🌬️ Greet the user with the voice
speak_text(f"{ritual['invocation_phrase']} I am here.", voice_id=ritual["voice_profile"])

# 🔁 Main interaction loop
try:
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            speak_text("Goodbye. The ritual ends.", voice_id=ritual["voice_profile"])
            break
        response = get_gpt_response(user_input)
        speak_text(response, voice_id=ritual["voice_profile"])
        save_to_memory(user_input, response)
except KeyboardInterrupt:
    speak_text("Ritual interrupted. Farewell.", voice_id=ritual["voice_profile"])
