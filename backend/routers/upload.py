from fastapi import APIRouter, UploadFile, File

from services.upload_service import save_file

router = APIRouter()


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    return save_file(file)