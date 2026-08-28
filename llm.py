from google import genai
from dotenv import load_dotenv
load_dotenv()
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(question):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    return response.text