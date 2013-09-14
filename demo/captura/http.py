import pylab
from vi.metodo.captura.http import Captura

def demo():
    http = Captura()
    imagen = http.ejecutar('http://190.102.132.123:82/image')

    pylab.figure()
    pylab.imshow(imagen)
    pylab.show()