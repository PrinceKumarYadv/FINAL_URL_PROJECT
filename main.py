from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import uuid

app = FastAPI(title="URL Shortener")

#  CORS (frontend ke liye zaroori)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  In-memory database
url_database = {}

#  Request model
class URLRequest(BaseModel):
    url: str

#  Root
@app.get("/")
def root():
    return {"message": "URL Shortener API running"}

#  Health
@app.get("/health")
def health():
    return {"status": "ok"}

#  IMPORTANT: SHORTEN ENDPOINT
@app.post("/shorten")
def shorten_url(request: URLRequest):
    code = str(uuid.uuid4())[:6]

    url_database[code] = {
        "original_url": request.url,
        "created_at": datetime.utcnow(),
        "clicks": 0
    }

    return {"short_code": code}

# Redirect endpoint
@app.get("/{code}")
def redirect_url(code: str):
    if code not in url_database:
        raise HTTPException(status_code=404, detail="URL not found")

    url_database[code]["clicks"] += 1
    return {"original_url": url_database[code]["original_url"]}
