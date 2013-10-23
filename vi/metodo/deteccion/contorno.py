# -*- coding: utf-8 -*-

"""Detección por búsqueda de contornos """
from __future__ import division

import numpy as np
import cv2


class Deteccion(object):
    """Detección de contornos """

    def __init__(self):
        """Inicia la lista de filtros """
        self.imagen = None
        def isfilter(attrname, methodclass):
            """¿El método es filtro? """
            return (attrname.startswith('filtro')
                    and hasattr(getattr(methodclass, attrname), '__class__'))
        self._filtros = [getattr(self, method) \
                         for method in dir(self) if isfilter(method, self)]

    def ejecutar(self, imagen):
        """Recibe una imagen y retorna una lista con las secciones limitadas
        por los contornos """
        self.imagen = imagen
        imgris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        _, umbral = cv2.threshold(imgris, 100, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(umbral,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_NONE)
        filtrados = []
        for contorno in contornos:
            if all(self.validar(contorno)):
                filtrados.append(contorno)

        regiones = [cv2.boundingRect(contorno) for contorno in filtrados]
        baldosas = [imagen[y:(y+dy), x:(x+dx)] for x, y, dx, dy in regiones]
        return baldosas

    def validar(self, contorno):
        """Devuelve un generador con valores booleanos por cada filtro

        >>> # Si hubieran dos filtros y el segundo falla
        >>> list(self.validar(contorno))
        [True, False]
        """
        return (filtrar(contorno) for filtrar in self._filtros)

    @staticmethod
    def filtro_a_num_pixel(contorno):
        """Filtro simple
        No considerar como válido porque solo aplica a la imagen de la demo
        """
        return 200 < len(contorno)

    @staticmethod
    def filtro_b_rect_horiz(contorno):
        """Verifica que el contorno contiene un rectángulo horizontal """
        _, _, ancho, alto = cv2.boundingRect(contorno)
        return alto < ancho/2.5

    def filtro_c_amarillo_blanco(self, contorno):
        """Filtro de color amarillo y blanco """
        imagen = self.imagen
        x, y, dx, dy = cv2.boundingRect(contorno)
        baldosa = imagen[y:(y+dy), x:(x+dx)]

        # _ = cv2.medianBlur(baldosa, 5)
        # hsv = cv2.cvtColor(baldosa, cv2.COLOR_BGR2HSV)
        hsv = baldosa

        a = cv2.inRange(hsv, np.array((20, 100, 100)), np.array((30, 255, 255)))
        b = cv2.inRange(hsv, np.array((100,100,10)), np.array((130, 130, 130)))
        mascara = cv2.add(a, b)

        erode = cv2.erode(mascara, None, iterations=1)
        dilate = cv2.dilate(erode, None, iterations=3)

        dilate = cv2.cvtColor(dilate, cv2.COLOR_GRAY2BGR)

        num_neg = (dilate == 0).sum()
        num_pos = dilate.size - num_neg
        ratio = num_pos/dilate.size

        # if ratio > 0.7:
        #     cv2.imshow('vii', np.hstack((dilate, hsv)))
        #     cv2.waitKey()

        return ratio > 0.7
