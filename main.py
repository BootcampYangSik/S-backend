
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Shrimp Feeding Test API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class TestMessage(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/v1/feeds/summary")
def get_feed_summary():
    return {
        "session_id": 1,
        "remaining_feed_percent": 42.5,
        "status": "feeding"
    }

@app.post("/api/v1/feeds/test")
def test_connection(data: TestMessage):
    return {
        "success": True,
        "received_message": data.message
    }
