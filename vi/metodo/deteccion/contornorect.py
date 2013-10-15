# -*- coding: utf-8 -*-

"""Detección por búsqueda de contornos rectangulares horizontales"""

from __future__ import division

import cv2
import vi.metodo.deteccion.contorno as padre


class Deteccion(padre.Deteccion):
    """Detección con filtro para zona reactangulares horizontales """

    def __init__(self):
        """Agrega el filtro """
        super(Deteccion, self).__init__()
        self._filtros.append(self.filtro_recthorizontal)

    @staticmethod
    def filtro_recthorizontal(contorno):
        """Verifica que el contorno contiene un rectángulo horizontal """
        _, _, ancho, alto = cv2.boundingRect(contorno)
        return alto < ancho/2.5