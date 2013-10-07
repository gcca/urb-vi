import cv2

class Captura(object):
    """
    Captura imagen
    """
    def __init__(self, ruta):
        try:
            self.fuente = ruta
        except IOError:
            raise AttributeError
    
    def ejecutar(self):
        """
        Rets:
            la imagen de la ruta especificada
        """

        fuente = self.fuente
        imagen = cv2.imread(fuente)
        return imagen