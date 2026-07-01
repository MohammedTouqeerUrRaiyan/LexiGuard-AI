import cv2 # pyright: ignore[reportMissingImports]
import pytesseract
def ocr (image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)
    return text


import cv2
import pytesseract
import numpy as np

# Uncomment for Windows
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -------------------------
# Load Image
# -------------------------
image = cv2.imread("images.png")

if image is None:
    print("Image not found.")
    exit()

# -------------------------
# Resize image
# -------------------------
scale_percent = 200

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

image = cv2.resize(image, (width, height))

# -------------------------
# Convert to grayscale
# -------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -------------------------
# Remove Noise
# -------------------------
gray = cv2.GaussianBlur(gray, (5,5), 0)

# -------------------------
# Thresholding
# -------------------------
binary = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    31,
    15
)

# -------------------------
# OCR Configuration
# -------------------------
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(binary, config=custom_config)

print("Detected Text")
print("-"*40)
print(text)

# -------------------------
# Get OCR Data
# -------------------------
data = pytesseract.image_to_data(
    binary,
    output_type=pytesseract.Output.DICT,
    config=custom_config
)

# -------------------------
# Draw Bounding Boxes
# -------------------------
for i in range(len(data['text'])):

    word = data['text'][i]
    confidence = int(float(data['conf'][i]))

    if confidence > 60 and word.strip() != "":

        x = data['left'][i]
        y = data['top'][i]
        w = data['width'][i]
        h = data['height'][i]

        cv2.rectangle(image,
                      (x,y),
                      (x+w,y+h),
                      (0,255,0),
                      2)

        cv2.putText(image,
                    word,
                    (x,y-5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0,0,255),
                    2)

cv2.imshow("OCR Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
