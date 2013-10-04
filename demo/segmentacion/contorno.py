import cv2
from vi.metodo.segmentacion.contorno1 import Segmentacion

def demo():
    imagen = cv2.imread('demo/segmentacion/carro2.jpg')
    contorno = Segmentacion()
    baldosas = contorno.ejecutar(imagen)

    for baldosa in baldosas:
        cv2.imshow('imagen', baldosa)
        cv2.waitKey()
