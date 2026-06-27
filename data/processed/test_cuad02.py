import os
import re
from datasets import load_dataset
import pdfplumber

# Dynamically finds the exact directory where THIS script is saved
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_DIR = CURRENT_DIR # Saves right next to this script

print("🔄 Fetching CUAD instance from Hugging Face cache...")
dataset = load_dataset("theatticusproject/cuad", verification_mode="no_checks")

# Grab the first contract asset entry
item = dataset['train'][0]
pdf_data = item['pdf']

# Get the path to the cached PDF file
source_path = getattr(pdf_data, 'path', None) or str(pdf_data)

if source_path and os.path.exists(source_path):
    filename = os.path.basename(source_path)
    txt_filename = filename.replace(".pdf", "_extracted.txt")
    output_path = os.path.join(PROCESSED_DIR, txt_filename)
    
    print(f"📖 Extracting text from: {filename}...")
    
    extracted_text = []
    total_pages = 0
    
    with pdfplumber.open(source_path) as pdf:
        total_pages = len(pdf.pages)
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                extracted_text.append(f"--- PAGE {page_num} ---\n{text}\n")
    
    full_document_text = "\n".join(extracted_text)
    
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(full_document_text)
        
    print("\n✨ Text Processing Pipeline Success!")
    print(f"✅ Extracted contract text saved to: {txt_filename}")
    
    # Data summary blocks
    lines = full_document_text.splitlines()
    words = full_document_text.split()
    potential_clauses = re.findall(r'(?:Section\s+\d+|Article\s+[IVXLCDM]+|\d+\.\d+)', full_document_text)
    
    print("\n==================================================")
    print("           LEXIGUARD DATA METRICS REPORT          ")
    print("==================================================")
    print(f" 📂 Target Folder   : {PROCESSED_DIR}")
    print(f" 📄 Source Document : {filename}")
    print(f" 📑 Total Pages     : {total_pages}")
    print(f" 📝 Line Count      : {len(lines)} structured lines")
    print(f" 🔤 Word Count      : {len(words)} total words")
    print(f" 🧮 Character Count : {len(full_document_text)} characters")
    print(f" ⚖️ Found Clauses   : Approx. {len(set(potential_clauses))} unique sections")
    print("==================================================")
    print(" 🚀 Pipeline status: IDLE | Ready for NLP parsing.")
    print("==================================================")

else:
    print("❌ Unable to locate local cached PDF data path.")