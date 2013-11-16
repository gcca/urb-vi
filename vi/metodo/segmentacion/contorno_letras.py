# encoding: utf-8

"""Segmetación por búsqueda de contornos """

from __future__ import division

import cv2
import numpy as np
import vi.metodo.segmentacion.contorno_base as contorno_base


class Segmentacion(contorno_base.Segmentacion):
    """Segmentación con filtro por área media """

    def __init__(self):
        """Agrega el procesador """
        super(Segmentacion, self).__init__()
        self._procesadores = [self.procesador_areamedia]

    def procesador_areamedia(self, baldosa):
        """En base al promedio, retira elementos que podrían no ser letras """

        gris, filtrados = self._filtro_area(baldosa)

        marcos = []
        if len(filtrados) > 4:
            regiones = [cv2.boundingRect(contorno) for contorno in filtrados]
            _, binario = cv2.threshold(gris, 90, 255, cv2.THRESH_BINARY_INV)
            letras = [binario[y:(y+dy), x:(x+dx)] for x, y, dx, dy in regiones]

            base = 1
            total = 2*base
            factor = 1.5

            for letra in letras:
                alto, ancho = letra.shape
                zoom = cv2.resize(letra, (int(factor*alto), int(factor*ancho)))
                alto, ancho = zoom.shape
                extra = np.zeros((alto+total, ancho+total), np.uint8)
                extra[base:alto+base, base:ancho+base] = zoom
                zoom = extra
                marcos.append(zoom)

        return marcos
