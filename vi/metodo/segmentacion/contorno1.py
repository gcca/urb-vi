# -*- coding: utf-8 -*-

"""Segmetación por búsqueda de contornos """

from __future__ import division

import cv2
import contorno0

class Segmentacion(contorno0.Segmentacion):

    def __init__(self):
        """Agrega el filtro """
        super(Segmentacion, self).__init__()
        self.filtros.append(self.filtro_rectHorizonal)

    def filtro_rectHorizonal(self, contorno):
        """Verifica que el contorno contiene un rectángulo horizontal """
        _, _, dx, dy = cv2.boundingRect(contorno)
        return dy < dx/2.5
