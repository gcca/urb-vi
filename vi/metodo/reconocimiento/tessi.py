# encoding: utf-8

import cv2.cv as cv
import tesseract
import re
import locale


class Reconocimiento(object):

    def __init__(self):
        locale.setlocale(locale.LC_NUMERIC, 'C')

    def ejecutar(self, baldosas):
        return [self.leerPlaca(baldosa) for baldosa in baldosas]

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
        api.Init('.', 'eng', tesseract.OEM_DEFAULT)
        api.SetVariable("tessedit_char_whitelist",
                        "0123456789ABCDFGHIJKLMNOPQRSTVWXYZ-UE")
        api.SetPageSegMode(tesseract.PSM_AUTO)

        # Enviando imagen binarizada al tesseract
        tesseract.SetCvImage(imgbincv, api)
        text = api.GetUTF8Text()
        text = re.sub(r'\W+', '', text)
        return text
