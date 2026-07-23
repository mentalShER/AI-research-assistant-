from fastapi import UploadFile
import os
import shutil

from utils.text_chunker import chunk_text
from utils.pdf_extractor import extract_text
from embeddings.embedding_service import generate_embeddings


UPLOAD_FOLDER = "uploads"


def save_file(file: UploadFile):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text, pages = extract_text(file_path)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    return {
    "filename": file.filename,
    "pages": pages,
    "characters": len(text),
    "chunks": len(chunks),
    "embeddings": len(embeddings)
}