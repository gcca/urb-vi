import cv2.cv as cv
import cv2
import pylab
from vi.metodo.deteccion.tesseractOCR import Deteccion

def demo():
	i=cv2.imread('demo/deteccion/eurotext.jpg')
	OCR=Deteccion()
	texto = OCR.ejecutar(i);
	print texto
