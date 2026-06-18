from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(
    title="LexiGuard AI",
    description="AI-Powered Contract Intelligence Platform",
    version="1.0.0"
)
class ContractRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "project": "LexiGuard AI",
        "module": "API & Integration",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "LexiGuard AI API"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }

@app.post("/analyze")
def analyze(data: ContractRequest):
    text = data.text

    keywords = [
        "agreement",
        "terminated",
        "termination",
        "notice",
        "payment",
        "liability",
        "confidential",
        "warranty"
    ]

    found_keywords = []

    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_keywords.append(keyword)

    return {
        "received_text": text,
        "word_count": len(text.split()),
        "character_count": len(text),
        "keywords_found": found_keywords,
        "status": "Analysis complete"
    }