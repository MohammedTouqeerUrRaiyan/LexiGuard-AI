import cv2 # pyright: ignore[reportMissingImports]
import pytesseract
def ocr (image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)
    return text
#improvise code

