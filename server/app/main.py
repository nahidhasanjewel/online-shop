from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online Shop API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Online Shop API is running! 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}