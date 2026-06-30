from fastapi import FastAPI, UploadFile, File
from src.ocr.ocr_pipeline import OCRPipeline
from src.ner.ner_pipeline import LegalNERPipeline
from src.analyzer.contract_analyzer import ContractAnalyzer

import os
import shutil

app = FastAPI(
    title="LexiGuard AI",
    description="AI Powered Contract Intelligence Platform",
    version="3.0"
)

# ----------------------------------------------------
# Initialize Pipelines
# ----------------------------------------------------

ocr = OCRPipeline()
ner = LegalNERPipeline()
analyzer = ContractAnalyzer()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------------------------------
# Routes
# ----------------------------------------------------

@app.get("/")
def home():

    return {
        "project": "LexiGuard AI",
        "version": "3.0",
        "status": "Running"
    }


@app.get("/health")
def health():

    return {
        "status": "Healthy"
    }


# ----------------------------------------------------
# Main Analysis Endpoint
# ----------------------------------------------------

@app.post("/analyze")
async def analyze_contract(file: UploadFile = File(...)):

    # ---------------------------------------
    # Save uploaded file
    # ---------------------------------------

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ---------------------------------------
    # OCR
    # ---------------------------------------

    extracted_text = ocr.extract(filepath)

    if not extracted_text.strip():

        return {
            "status": "Failed",
            "message": "No readable text found."
        }

    # ---------------------------------------
    # Named Entity Recognition
    # ---------------------------------------

    entities = ner.extract_entities(
        extracted_text
    )

    # ---------------------------------------
    # Contract Intelligence
    # ---------------------------------------

    analysis = analyzer.analyze(
        extracted_text
    )

    # ---------------------------------------
    # Final Response
    # ---------------------------------------

    return {

        "status": "Analysis Complete",

        "filename": file.filename,

        "entities_detected": entities,

        "extracted_text": extracted_text,

        **analysis

    }