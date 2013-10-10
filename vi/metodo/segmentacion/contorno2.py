# encoding: utf-8

"""Segmetación por búsqueda de contornos """

from __future__ import division

import cv2
import numpy as np
import vi.metodo.segmentacion.contorno1 as contorno1

class Segmentacion(contorno1.Segmentacion):
    """Segmentación con filtro por área media """

    def __init__(self):
        """Agrega el procesador """
        super(Segmentacion, self).__init__()
        self._procesadores.append(self.procesador_areamedia)

    @staticmethod
    def procesador_areamedia(baldosa):
        """En base al promedio, retira elementos que podrían no ser letras """
        gris = cv2.cvtColor(baldosa, cv2.COLOR_BGR2GRAY)
        _, binarizado = cv2.threshold(gris, 90, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(binarizado,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

        mask = np.zeros(gris.shape, np.uint8)
        areas = [cv2.contourArea(c) for c in contornos]
        mu = np.array(areas).mean()

        filtrados = []
        for contorno, area in zip(contornos, areas):
            if 50 < area < mu:
                filtrados.append(contorno)

        cv2.drawContours(mask, filtrados, -1, 255, -1)
        binarizado = mask

        binarizado = cv2.cvtColor(binarizado, cv2.COLOR_GRAY2BGR)

        return binarizado
