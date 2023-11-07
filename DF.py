import pytesseract
from PIL import Image

# Open the image file.
image = Image.open("image.png")

# Perform OCR using Tesseract.
text = pytesseract.image_to_string(image)

# Print the extracted text.
print(text)