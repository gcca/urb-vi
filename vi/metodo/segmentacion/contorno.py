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

        mascara = np.zeros(gris.shape, np.uint8)
        cv2.drawContours(mascara, filtrados, -1, 255, 1)

        shape = (gris.shape[0] + 10, gris.shape[1] + 10)
        marco = np.zeros(shape, np.uint8)
        marco[5:gris.shape[0]+5, 5:gris.shape[1]+5] = mascara

        return marco
