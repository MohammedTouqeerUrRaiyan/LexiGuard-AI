from fastapi import FastAPI, UploadFile, File
from src.ocr.ocr_pipeline import OCRPipeline
from src.ner.ner_pipeline import LegalNERPipeline  # 1. Import your new pipeline module
import os
import shutil

app = FastAPI(
    title="LexiGuard AI",
    description="AI Powered Contract Intelligence",
    version="2.0"
)

ocr = OCRPipeline()
ner = LegalNERPipeline()  # 2. Instantiate your entity extraction engine

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "project": "LexiGuard AI",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = ocr.extract(filepath)
    
    # 3. Feed the raw text straight into your new NER tool
    entities_found = ner.extract_entities(extracted_text)

    processed = extracted_text.lower()

    clause_rules = {
        "Termination Clause": ["terminate", "termination", "notice period"],
        "Confidentiality Clause": ["confidential", "non-disclosure", "nda"],
        "Payment Clause": ["payment", "invoice", "fee"],
        "Liability Clause": ["liability", "indemnify", "damages"],
        "Warranty Clause": ["warranty", "guarantee"],
        "Arbitration Clause": ["arbitration", "dispute resolution"]
    }

    clauses = []
    keywords = []

    for clause, words in clause_rules.items():
        found = False
        for word in words:
            if word in processed:
                keywords.append(word)
                found = True
        if found:
            clauses.append(clause)

    risk = "Low"
    if any(x in keywords for x in ["terminate", "termination"]):
        risk = "Medium"
    if any(x in keywords for x in ["liability", "damages", "indemnify"]):
        risk = "High"

    return {
        "filename": file.filename,
        "word_count": len(extracted_text.split()),
        "character_count": len(extracted_text),
        "keywords_found": list(set(keywords)),
        "clauses_detected": clauses,
        "risk_level": risk,
        "entities_detected": entities_found,  # 4. Injected clean structured entity array here
        "extracted_text": extracted_text,
        "status": "Analysis Complete"
    }