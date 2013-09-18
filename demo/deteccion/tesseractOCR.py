import cv2
from vi.metodo.deteccion.tesseractOCR import Deteccion

def demo():
    i = cv2.imread('demo/deteccion/eurotext.jpg')
    OCR = Deteccion()
    texto = OCR.ejecutar(i);
    print(texto)
