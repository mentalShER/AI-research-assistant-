from google import genai
from core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_embedding(text: str) -> list[float]:
    response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
 )

    return response.embeddings[0].values


def generate_embeddings(chunks: list[str]):
    embeddings = []

    for chunk in chunks:
        vector = generate_embedding(chunk)

        embeddings.append({
            "text": chunk,
            "embedding": vector
        })

    return embeddings