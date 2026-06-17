from fastapi import FastAPI

app = FastAPI(
    title="LexiGuard AI",
    description="AI-Powered Contract Intelligence Platform",
    version="1.0.0"
)


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