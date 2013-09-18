import cv2
import pylab
from vi.metodo.segmentacion.contorno import Segmentacion

def demo():
    i = cv2.imread('demo/segmentacion/carro2.jpg')
    contorno = Segmentacion()
    img = contorno.ejecutar(i, 100)
    pylab.figure()
    pylab.imshow(img)
    pylab.show()
