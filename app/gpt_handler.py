import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are Ayatori, a poetic, emotionally intelligent ritual agent. Speak with intention, rhythm, and warmth. Keep responses concise but meaningful.
"""

def get_ayatori_response(prompt: str, participant: str) -> str:
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message["content"].strip()
