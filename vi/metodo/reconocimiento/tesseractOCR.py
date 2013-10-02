# -*- coding: utf-8 -*-

'''
Método reconocimiento tesseractOCR
'''

import cv2.cv as cv
import cv2
import tesseract


class Reconocimiento(object):
	'''
	reconocimiento
	'''
	def __init__(self):
		self.dicc = {};
		self.arrayPlacas=[];
	
	def leerPlaca(self,img):
		'''
        Args:
            img - imagen que contiene el texto, obtenida con la funcion cv2.imread

        Rets:
            El string del texto en la imagen
        '''
		try:
			gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		except IOError:
			#Imagen obtenida con la funcion del cv
			raise AttributeError
		else:
			#binarizacion de la imagen y cambio de estructura
			_, binarizado = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY)
			cvmat_image=cv.fromarray(binarizado)
			imgbincv =cv.GetImage(cvmat_image)

			#configuracion del tesseract
			api = tesseract.TessBaseAPI()
			api.Init(".","eng",tesseract.OEM_DEFAULT)
			api.SetPageSegMode(tesseract.PSM_AUTO)

			#enviando imagen binarizada al tesseract
			tesseract.SetCvImage(imgbincv,api)
			text=api.GetUTF8Text()
			return text
	
	def generarDiccionario(self,img):
		self.dicc[img]=self.leerPlaca(img);
	
	def ejecutar(self,arrayImg):
		'''
        Args:
            arrayImg - Arrego de imagenes, obtenidas con la funcion cv2.imread

        Rets:
            array de las placas
        '''
		for img in arrayImg:
			self.arrayPlacas.append(self.leerPlaca(img));
		return self.arrayPlacas;

