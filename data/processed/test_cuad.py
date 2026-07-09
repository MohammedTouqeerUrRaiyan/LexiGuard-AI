#It's a useful data-ingestion utility.
import os
import shutil
from datasets import load_dataset

# Target directory path
PROCESSED_DIR = r"E:\intern\zaalima\LexiGuard-AI\data\processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

print("🔄 Fetching CUAD instance from Hugging Face cache...")
dataset = load_dataset("theatticusproject/cuad", verification_mode="no_checks")

# store the first contract asset row entry in a variable 
item = dataset['train'][0]
pdf_data = item['pdf']

# Handle custom Hugging Face PDF object structural layers cleanly
try:
    # Read the direct internal path attribute of the HF PDF object
    source_path = getattr(pdf_data, 'path', None)
    
    # Fallback check if it maps down as a direct string pathing
    if not source_path:
        source_path = str(pdf_data)

    if source_path and os.path.exists(source_path):
        filename = os.path.basename(source_path)
        output_path = os.path.join(PROCESSED_DIR, filename)
        
        # Copy the raw source PDF right over to your processed workspace
        shutil.copy(source_path, output_path)
        print("\n✨ Extraction Pipeline Success!")
        print(f"✅ Copied source contract: {filename}")
        print(f"👉 Saved to: {output_path}")
    else:
        print("❌ Unable to resolve local cached location path from dataset object.")

except Exception as e:
    print(f"❌ An error occurred during file extraction lookup: {str(e)}")