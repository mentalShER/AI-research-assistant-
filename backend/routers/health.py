from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "AI-research-assistant"}

@router.get("/health")
def read_root():
    return {"status": "healthy"}

@router.get("/version")
def read_root():
    return {"version": "1.0.0"}