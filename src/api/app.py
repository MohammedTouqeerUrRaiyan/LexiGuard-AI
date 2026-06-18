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
    clauses = []


    text = data.text.lower()

    clause_rules = {
        "Termination Clause": [
            "terminate", "terminated", "termination", "notice period", "end of agreement"
        ],
        "Confidentiality Clause": [
            "confidential", "nda", "non-disclosure"
        ],
        "Payment Clause": [
            "payment", "invoice", "fee", "billing"
        ],
        "Liability Clause": [
            "liability", "indemnify", "damages"
        ],
        "Warranty Clause": [
            "warranty", "guarantee"
        ],
        "Arbitration Clause": [
            "arbitration", "dispute resolution"
        ]
    }

    clauses_detected = []

    for clause_name, keywords in clause_rules.items():
        if any(k in text for k in keywords):
            clauses_detected.append(clause_name)

    found_keywords = []

    if "termination" in text or "terminated" in text:
        clauses.append("Termination Clause")

    if "confidential" in text:
        clauses.append("Confidentiality Clause")

    if "payment" in text:
        clauses.append("Payment Clause")

    if "liability" in text:
        clauses.append("Liability Clause")

    if "warranty" in text:
        clauses.append("Warranty Clause")

    if "arbitration" in text:
        clauses.append("Arbitration Clause")

    for keyword in keywords:
        if keyword.lower() in text.lower():
            found_keywords.append(keyword)
        risk_level = "Low"

        if "terminated" in found_keywords:
            risk_level = "Medium"

        if "liability" in found_keywords:
            risk_level = "High"

    return {
        "received_text": data.text,
        "word_count": len(data.text.split()),
        "character_count": len(data.text),
        "keywords_found": found_keywords,
        "clauses_detected": clauses_detected,   # 🔥 THIS IS KEY
        "risk_level": risk_level,
        "status": "Analysis complete"
    }