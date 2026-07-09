from fastapi import FastAPI, UploadFile, File
from src.embeddings.semantic_search import SemanticSearch
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
semantic_search = SemanticSearch()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------------------------------
# Base Routes
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

    # 1. Save uploaded file safely
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2. Extract text using OCR Pipeline
    extracted_text = ocr.extract(filepath)

    if not extracted_text or not extracted_text.strip():
        return {
            "status": "Failed",
            "message": "No readable text found or document is blank."
        }

    # 3. Named Entity Recognition
    entities = ner.extract_entities(extracted_text)

    # 4. Contract Intelligence Analysis
    analysis = analyzer.analyze(extracted_text)
    
    # 5. Populate and run Semantic Search
    semantic_search.load_documents([
        {
            "text": clause["description"],
            "metadata": {"clause": clause["clause"]}
        }
        for clause in analysis.get("clauses", {}).get("detected", [])
    ])
    
    semantic_matches = semantic_search.search(extracted_text, top_k=5)

    # 6. Structured Final Response (No massive raw data leaks)
    return {
        "status": "Analysis Complete",
        "filename": file.filename,
        "entities_detected": entities,
        "semantic_matches": semantic_matches,
        "analysis_results": {
            "detected_clauses": analysis.get("clauses", {}).get("detected", []),
            "missing_clauses": analysis.get("statistics", {}).get("missing_clauses", 0),
            "risk_score": analysis.get("risk_score", "Low")
        }
    }