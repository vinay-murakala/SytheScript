import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-pro")
    
from vertexai.preview.language_models import TextGenerationModel

def run_gemini_qa(context: str, question: str) -> str:
    model = TextGenerationModel.from_pretrained("gemini-1.5-pro-preview")
    prompt = f"""You are an intelligent assistant. Use the below context to answer the question.

Context:
{context}

Question:
{question}

Answer:"""

    response = model.predict(
        prompt=prompt,
        max_output_tokens=512,
        temperature=0.3
    )
    return response.text.strip()

