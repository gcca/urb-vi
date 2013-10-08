"""Babas de captura """
import os
import cv2

class Captura(object):
    """Lee imagen desde un fichero """

    @staticmethod
    def ejecutar(ruta):
        """Retorna la imagen de la `ruta` """
        if not os.path.exists(ruta):
            raise ValueError('No existe el fichero con ruta ' + ruta)

        imagen = cv2.imread(ruta)
        return imagen
