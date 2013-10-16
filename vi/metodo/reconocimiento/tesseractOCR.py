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
        api.SetPageSegMode(tesseract.PSM_AUTO)

        # Enviando imagen binarizada al tesseract
        tesseract.SetCvImage(imgbincv, api)
        text = api.GetUTF8Text()
        text = re.sub(r'\W+', '', text)
        return text

    def ejecutar(self, baldosas):
        """
        Args:
            arrayImg - Arrego de imagenes, obtenidas con la funcion cv2.imread

        Rets:
            array de las placas
        """
        return [self.leerPlaca(baldosa) for baldosa in baldosas]
