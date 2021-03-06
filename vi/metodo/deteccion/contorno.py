# encoding: utf-8

"""Detección por búsqueda de contornos."""
from __future__ import division, print_function

import numpy as np
import cv2
from vi.util import dibujar_rectangulos, dibujar_contornos, \
    generar_umbrales, hallar_contornos


class Deteccion(object):
    """Detección de contornos."""

    def __init__(self):
        """Inicia la lista de filtros."""
        self.imagen = None

        def isfilter(attrname, methodclass):
            """¿El método es filtro?."""
            return (attrname.startswith('filtro')
                    and hasattr(getattr(methodclass, attrname), '__class__'))

        self._filtros = [getattr(self, method)
                         for method in dir(self) if isfilter(method, self)]

    def ejecutar(self, imagen):
        """Recibe una imagen y retorna una lista con las secciones limitadas
        por los contornos."""
        self.imagen = self.suavizar(imagen)
        contornos = self.__contornos()

        # filtrados = (self.__aplicar_filtros(contornos)
        #              if __debug__
        #              else [c for c in contornos if all(self.validar(c))])
        filtrados = [c for c in contornos if all(self.validar(c))]
        regiones = [cv2.boundingRect(contorno) for contorno in filtrados]
        baldosas = [imagen[y:(y+dy), x:(x+dx)] for x, y, dx, dy in regiones]
        return baldosas

    def suavizar(self, img):
        return cv2.bilateralFilter(img, 29, 58, 14.5)

    def __contornos(self):
        """Obtener contornos de la imagen."""
        umbrales = generar_umbrales(self.imagen, 13, 6, 31, 4)
        contornos = hallar_contornos(umbrales,
                                     cv2.RETR_TREE,
                                     cv2.CHAIN_APPROX_NONE)

        # if __debug__:
        #     print('2. Contornos')
        #     img_tmp = self.imagen.copy()
        #     dibujar_contornos(img_tmp, contornos)
        #     cv2.imshow('det', img_tmp)
        #     cv2.waitKey()

        return contornos

    # def __aplicar_filtros(self, contornos):
    #     """Depuración: Aplicar filtros."""
    #     print('3.')
    #     i = 0
    #     filtrados = contornos
    #     for filtro in self._filtros:
    #         contornos = filtrados
    #         filtrados = []
    #         for contorno in contornos:
    #             if filtro(contorno):
    #                 filtrados.append(contorno)
    #         i += 1
    #         print('  3.%s %s' % (i, filtro.__name__))
    #         contornos = filtrados
    #         tmp = self.imagen.copy()
    #         dibujar_rectangulos(tmp, contornos)
    #         cv2.imshow('det', tmp)
    #         cv2.waitKey()
    #     return filtrados

    def validar(self, contorno):
        """Devuelve un generador con valores booleanos por cada filtro

        >>> # Si hubieran dos filtros y el segundo falla
        >>> list(self.validar(contorno))
        [True, False]
        """
        return (filtrar(contorno) for filtrar in self._filtros)

    def filtro_a(self, contorno):
        """Filtro simple
        No considerar como válido porque solo aplica a la imagen de la demo.
        """
        return 60 < len(contorno)

    def filtro_b(self, contorno):
        """Verifica que el contorno contiene un rectángulo horizontal."""
        _, _, ancho, alto = cv2.boundingRect(contorno)
        return ancho <= 5*alto and ancho > 1.5*alto

    def filtro_c(self, contorno):
        """Filtro blanco - amarillo."""
        x, y, dx, dy = cv2.boundingRect(contorno)
        hsv = self.imagen[y:(y+dy), x:(x+dx)]
        hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
        hsv = cv2.GaussianBlur(hsv, (3, 3), 0)
        # blanco, amarillo
        mascara = cv2.add(cv2.inRange(hsv,
                                      np.array((  0,   0,  90), np.uint8),
                                      np.array((180, 100, 255), np.uint8)),
                          cv2.inRange(hsv,
                                      np.array(( 10, 100, 100), np.uint8),
                                      np.array(( 40, 255, 255), np.uint8)))
        erode = cv2.erode(mascara, None, iterations=1)
        dilate = cv2.dilate(erode, None, iterations=3)
        num_neg = (dilate == 0).sum()
        num_pos = dilate.size - num_neg
        ratio = num_pos/dilate.size
        return ratio > 0.5

    def filtro_d(self, contorno):
        """Filtro por número de contornos internos. Pretende estimar
        la cantidad de posibles letras."""
        x, y, dx, dy = cv2.boundingRect(contorno)
        baldosa = self.imagen[y:(y+dy), x:(x+dx)]
        umbrales = generar_umbrales(baldosa, 35, 7, 39, 5)
        mezcla = [cv2.findContours(umbral,
                                   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
                  for umbral in umbrales]

        for contornos in mezcla:
            if len(contornos) < 6:
                return False

        return True
