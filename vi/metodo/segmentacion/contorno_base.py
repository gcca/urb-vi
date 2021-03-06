# encoding: utf-8

"""Segmetación por búsqueda de contornos """

from __future__ import division

import cv2
import numpy as np
# from itertools import izip
from vi.util import generar_umbrales, hallar_contornos


class Segmentacion(object):
    """Segmentación con filtro por área media """

    def __init__(self):
        """Agrega el procesador """
        super(Segmentacion, self).__init__()
        self._procesadores = []

    def ejecutar(self, baldosas):
        """Recibe una lista de baldosas para ser pre-procesadas y mejorar
        la lectura de los caracteres. Retorna la lista de baldosas procesadas.
        """
        return [self._procesar(baldosa) for baldosa in baldosas]

    def _procesar(self, baldosa):
        """Aplica los pre-procesadores a la baldosa. """
        procesada = baldosa
        for procesador in self._procesadores:
            procesada = procesador(procesada)
        return procesada

    @staticmethod
    def _filtro_area(baldosa):
        """En base al promedio, retira elementos que podrían no ser letras

        Returns:
            baldosa_gris, filtrados: Baldosa en escala de grises y contornos
                filtrados por su área.
        """
        gris = cv2.cvtColor(baldosa, cv2.COLOR_BGR2GRAY)
        umbrales = generar_umbrales(baldosa, 13, 6, 31, 4)
        contornos = hallar_contornos(umbrales,
                                     cv2.RETR_TREE,
                                     cv2.CHAIN_APPROX_NONE)
        filtrados = []
        if len(contornos) > 5:
            areas = [cv2.contourArea(c) for c in contornos]
            d_areas = np.array(areas)
            mu = d_areas.mean()
            sigma = d_areas.std()
            for contorno, area in zip(contornos, areas):
                if mu - sigma < area < mu - 0.09*sigma:
                    filtrados.append(contorno)
        # tmp = baldosa.copy()
        # dibujar_contornos(tmp, filtrados)
        # cv2.imshow('seg', tmp)
        # cv2.waitKey()

        return gris, filtrados

        # mascara = np.zeros(gris.shape, np.uint8)
        # cv2.drawContours(mascara, filtrados, -1, 255, 1)

        # shape = (gris.shape[0] + 10, gris.shape[1] + 10)
        # marco = np.zeros(shape, np.uint8)
        # marco[5:gris.shape[0]+5, 5:gris.shape[1]+5] = mascara

        # # _, binarizado_base = cv2.threshold(gris, 90, 255, cv2.THRESH_BINARY)
        # # diff = cv2.absdiff(binarizado_base, mascara)
        # # cv2.imshow('video', diff)
        # # cv2.waitKey()

        # # shape = tuple(sum(x) for x in izip(baldosa.shape, (10, 10, 0)))
        # # bald = np.zeros(shape, np.uint8)
        # # bald[:baldosa.shape[0], :baldosa.shape[1]] = baldosa
        # # masc = cv2.cvtColor(marco, cv2.COLOR_GRAY2BGR)
        # # cv2.imshow('video', np.hstack((bald, masc)))
        # # cv2.waitKey()

        # return marco
