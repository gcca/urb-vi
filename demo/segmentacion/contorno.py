# encoding: utf-8
"""
Demo de segmentación por contornos
"""
import cv2
from vi.metodo.segmentacion.contorno import Segmentacion

def demo():
    """Lee imagen y lista las regiones donde podrían existir placas """
    imagen = cv2.imread('demo/segmentacion/carro2.jpg')
    contorno = Segmentacion()
    baldosas = contorno.ejecutar(imagen)

    for baldosa in baldosas:
        cv2.imshow('imagen', baldosa)
        cv2.waitKey()
