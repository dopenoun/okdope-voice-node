import json
import os
from datetime import datetime

def log_interaction(participant: str, user_input: str, response: str):
    log_dir = "memory"
    os.makedirs(log_dir, exist_ok=True)
    file_path = os.path.join(log_dir, f"{participant}_ritual.json")

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "participant": participant,
        "message": user_input,
        "response": response
    }

    if os.path.exists(file_path):
        with open(file_path, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)
    else:
        with open(file_path, "w") as f:
            json.dump([entry], f, indent=2)
