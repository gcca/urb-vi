import pylab
from vi.metodo.captura.http import Captura

def demo():
    http = Captura('http://190.102.132.123:82/image')
    imagen = http.ejecutar()

    pylab.figure()
    pylab.imshow(imagen)
    pylab.show()
