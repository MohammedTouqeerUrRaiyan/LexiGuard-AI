# LexiGuard AI: AI-Powered Contract Intelligence & Risk Scoring

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/backend-FastAPI-009688)
![ML/NLP](https://img.shields.io/badge/NLP-Transformers%20%7C%20spaCy-6C5CE7)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📋 Project Overview
**LexiGuard AI** is an enterprise-grade NLP and Large Language Model (LLM)-powered platform engineered to automate legal contract analysis. By leveraging state-of-the-art transformer models, Named Entity Recognition (NER), and Vector Databases, the platform ingests unstructured legal documents (PDFs/Word) to extract critical entities, classify legal clauses, flag hidden liabilities, and enable sub-second semantic search across entire document repositories.

Designed for legal teams, compliance departments, and enterprises handling heavy document volumes, LexiGuard AI transforms slow, manual contract audits into an automated, risk-aware digital workflow.

> **Note**: This is a production-level, collaborative DSML internship project developed following industry-standard Git workflows and modular architecture.

---

## ⚠️ Problem Statement
Modern enterprise legal and compliance teams face a massive bottleneck: reviewing hundreds of complex, multi-page legal contracts manually. This manual process is:
* ⏳ **Time-Consuming & Costly:** High-billing-rate legal experts spend hours parsing standard clauses.
* ❌ **Prone to Human Error:** Oversight of critical terms, missing termination dates, or unrecognized governing jurisdictions can expose companies to severe financial and regulatory risk.
* 🗄️ **Information Silos:** Archiving contracts as flat PDFs makes it virtually impossible to rapidly search, compare, or query cross-document liabilities.

---

## 💡 The Solution
LexiGuard AI solves these operational bottlenecks by introducing an intelligent, automated pipeline that extracts insights from unstructured text. The system reads ingested legal documents, surfaces structural entities (e.g., specific dates, values, organizations), identifies standard vs. anomalous legal clauses, computes an automated Risk Score based on non-standard language, and indexes document vectors into a semantic search engine. This allows legal analysts to perform conceptual queries (e.g., *"Find all agreements with exposure to European data privacy liabilities"*) instantly.

---

## 🎥 System Demonstration
Below is a demonstration of the asynchronous ingestion pipeline processing a multi-page standard agreement, extracting compliance entities, and returning a calculated risk vector.

## System Pipeline

PDF → OCR → NER → Clause Classification → Risk Assessment → Embeddings → FastAPI → JSON Response
---

## ✨ Key Features
* 📄 **Robust Document Ingestion:** Production-ready OCR pipeline converting native or scanned PDFs and Word documents into clean, structured text.
* 🏷️ **Custom Named Entity Recognition (NER):** Automated extraction of critical legal variables, including governing jurisdictions, monetary values, contracting parties, and key dates.
* ⚖️ **Deep-Learning Clause Classification:** Fine-tuned transformer models that automatically segment text and isolate standard clauses (e.g., Indemnification, Confidentiality, Termination).
* 🚨 **Automated Risk Scoring Engine:** Algorithmic scoring that highlights unusual or high-risk language deviations against institutional baselines.
* 🔍 **Semantic Contract Search:** High-dimensional vector embeddings paired with a vector database to allow concept-based semantic discovery.
* 🚀 **Enterprise API & Async Processing:** A scalable FastAPI backend backed by a Celery task queue to process bulk legal documents asynchronously.
* 🐳 **Cloud-Native Deployment:** Fully containerized architecture using Docker, ready for seamless deployment to AWS EC2 or Kubernetes.

---

## 🛠️ Technology Stack

| Domain | Technologies Used |
| :--- | :--- |
| **Core Programming** | Python (3.10+) |
| **Machine Learning & NLP** | PyTorch, Hugging Face Transformers, spaCy, BERT / RoBERTa |
| **OCR & Document Ingestion**| Tesseract OCR, `pdf2image` |
| **Semantic Search & LLM** | LangChain, Pinecone / Milvus |
| **Backend & Orchestration** | FastAPI, Uvicorn, Celery, Redis |
| **DevOps & Infrastructure**| Docker, Git/GitHub, AWS EC2 |

---

## 🏗️ Project Architecture & Workflow
The platform processes data through a highly decoupled, modular pipeline to maximize throughput and maintainability: