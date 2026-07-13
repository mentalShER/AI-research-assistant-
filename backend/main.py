from fastapi import FastAPI
from routers.chat import router as chat_router
from routers.health import router as health_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(health_router)