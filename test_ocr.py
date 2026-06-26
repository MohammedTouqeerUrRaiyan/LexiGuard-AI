from src.ocr.ocr_pipeline import OCRPipeline

ocr = OCRPipeline()

file_path = r"E:\intern\zaalima\LexiGuard-AI\docs\employment_contract.pdf"   # Change this to your test file

text = ocr.extract(file_path)

print(text)