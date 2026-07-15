from llm.gemini import ask_gemini

def generate_reply(message: str):
    return ask_gemini(message)