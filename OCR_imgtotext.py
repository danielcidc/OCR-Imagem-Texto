import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Caminho para o Tesseract
def convert():
    img = Image.open('ponto.png')
    text = pytesseract.image_to_string(img)
    print(text)

convert()