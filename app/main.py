from fastapi import FastAPI
from app.routes import router
app = FastAPI(title="AI Meme & Poster Creator")
app.include_router(router)
