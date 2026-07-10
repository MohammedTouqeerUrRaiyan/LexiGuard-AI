import os
import cv2
import fitz
import pytesseract

# Change this if Tesseract is installed elsewhere
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class OCRPipeline:

    def extract_from_image(self, image_path: str):

        if not os.path.exists(image_path):
            raise FileNotFoundError(
    f"Image not found: {image_path}"
)

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError("Unable to read image.")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.GaussianBlur(gray, (3,3), 0)

        _, thresh = cv2.threshold(
        gray,
        0,
        255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
        text = pytesseract.image_to_string(thresh)
        text = pytesseract.image_to_string(gray)

        return text.strip()


    def extract_from_pdf(self, pdf_path: str):

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(pdf_path)

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        return text.strip()


    def extract(self, file_path: str):

        extension = os.path.splitext(file_path)[1].lower()

        if extension in [".png", ".jpg", ".jpeg"]:
            return self.extract_from_image(file_path)

        elif extension == ".pdf":
            return self.extract_from_pdf(file_path)

        else:
            raise ValueError("Unsupported file type.")