# -*- coding: utf-8 -*-

"""Segmetación por búsqueda de contornos """

from __future__ import division

import cv2
import vi.metodo.segmentacion.contorno0 as contorno0

class Segmentacion(contorno0.Segmentacion):
    """Segmentación con filtro para zona reactangulares horizontales """

    def __init__(self):
        """Agrega el filtro """
        super(Segmentacion, self).__init__()
        self.filtros.append(self.filtro_recthorizontal)

    @staticmethod
    def filtro_recthorizontal(contorno):
        """Verifica que el contorno contiene un rectángulo horizontal """
        _, _, ancho, alto = cv2.boundingRect(contorno)
        return alto < ancho/2.5
