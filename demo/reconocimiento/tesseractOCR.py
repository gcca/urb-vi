import cv2
from vi.metodo.reconocimiento.tesseractOCR import Reconocimiento

def demo():
    i = cv2.imread('demo/reconocimiento/eurotext.jpg')
    OCR = Reconocimiento()
    texto = OCR.ejecutar(i);
    print(texto)
