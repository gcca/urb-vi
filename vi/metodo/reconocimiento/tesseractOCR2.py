# encoding: utf-8

"""Método reconocimiento tesseractOCR. """

import re
from cv2 import cv
import tesseract

class Reconocimiento(object):
    """Reconocimiento. """

    def leerPlaca(self, binarizado):
        """
        Args:
            img: imagen que contiene el texto, obtenida con la
                funcion cv2.imread.
        Returns:
            El string del texto en la imagen.
        """
        cvmat_image = cv.fromarray(binarizado)
        imgbincv = cv.GetImage(cvmat_image)
        # GetImage fuente de un error, revisar

        # Configuración del tesseract
        api = tesseract.TessBaseAPI()
        api.Init(".", "eng", tesseract.OEM_DEFAULT)
        # PSM_SINGLE_CHAR para lectura caracter a caracter
        api.SetPageSegMode(tesseract.PSM_SINGLE_CHAR)

        # Enviando imagen binarizada al tesseract
        tesseract.SetCvImage(imgbincv, api)
        text = api.GetUTF8Text()        
        text = re.sub(r'\W+', '', text)        
        return text

    def ejecutar(self, baldosas):
        """
        Args:
            baldosas - Arreglo de posibles placas, que contienen un arreglo de letras 

        Rets:
            array de las placas
        """            
        placas = []
        for baldosa in baldosas:
            placas.append([self.leerPlaca(letra) for letra in baldosa])
        return placas