import cv2
from vi.metodo.reconocimiento.tesseractOCR import Reconocimiento

def demo():
    i = cv2.imread('demo/reconocimiento/eurotext.jpg');
    i2 = cv2.imread('demo/reconocimiento/ejemplo2.jpg');
    arrayImg = [];
    arrayImg.append(i);
    arrayImg.append(i2);
    OCR = Reconocimiento();    
    textos = OCR.ejecutar(arrayImg);
    for texto in textos:
        print(texto);
