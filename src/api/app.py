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
    raw_text = data.text
    processed_text = raw_text.lower()

    # Consolidated Multi-keyword Mapping Logic
    clause_rules = {
        "Termination Clause": ["terminate", "terminated", "termination", "notice period", "end of agreement"],
        "Confidentiality Clause": ["confidential", "nda", "non-disclosure"],
        "Payment Clause": ["payment", "invoice", "fee", "billing"],
        "Liability Clause": ["liability", "indemnify", "damages"],
        "Warranty Clause": ["warranty", "guarantee"],
        "Arbitration Clause": ["arbitration", "dispute resolution"]
    }

    clauses_detected = []
    found_keywords = []

    # Single efficient pass loop for detecting clauses and keywords
    for clause_name, target_keywords in clause_rules.items():
        clause_matched = False
        for kw in target_keywords:
            if kw in processed_text:
                found_keywords.append(kw)
                clause_matched = True
        if clause_matched:
            clauses_detected.append(clause_name)

    # Clean, scoped Risk Assessment Logic
    risk_level = "Low"
    if any(term in found_keywords for term in ["terminate", "terminated", "termination"]):
        risk_level = "Medium"
    if any(term in found_keywords for term in ["liability", "indemnify", "damages"]):
        risk_level = "High"

    return {
        "received_text": raw_text,
        "word_count": len(raw_text.split()),
        "character_count": len(raw_text),
        "keywords_found": list(set(found_keywords)),  # deduplicate keyword array
        "clauses_detected": clauses_detected,   
        "risk_level": risk_level,
        "status": "Analysis complete"
    }