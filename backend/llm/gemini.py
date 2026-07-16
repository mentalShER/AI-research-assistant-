from google import genai

from core.config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, I'm unable to process your request right now."