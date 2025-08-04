# agents/summarizer.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-pro")

def summarize_text(text: str) -> str:
    if not text.strip():
        return "❌ No text to summarize."

    prompt = (
        '''Summarize the following content in a detailed yet concise manner.
        Bullet Format is also fine\n\n'''
        f"{text[:10000]}"  # Gemini 1.5 can handle large context
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Failed to summarize: {e}"
