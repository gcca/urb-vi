# encoding: utf-8

from __future__ import division

import cv2
import numpy as np
import vi.util


class Segmentacion(object):
    """Segmentación con filtro por área media """

    def ejecutar(self, baldosas):
        """Método princpial."""
        return [c for c in [self.cortar(b) for b in baldosas] if c is not None]

    def cortar(self, baldosa):
        """Cortar la sección mínima con las letras.
        """
        # base
        gris = cv2.cvtColor(baldosa, cv2.COLOR_BGR2GRAY)
        umbral = cv2.adaptiveThreshold(gris,
                                       255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY_INV,
                                       19,
                                       0)

        c = 7
        dy, dx = umbral.shape
        umbral = cv2.resize(umbral, (int(c*dx), int(c*dy)))
        baldosa = cv2.resize(baldosa, (int(c*dx), int(c*dy)))

        estructura = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
        mascara = np.zeros(umbral.shape, np.uint8)
        while True:
            erosionado = cv2.erode(umbral, estructura)
            temp = cv2.dilate(erosionado, estructura)
            temp = cv2.subtract(umbral, temp)
            mascara = cv2.bitwise_or(mascara, temp)
            umbral = erosionado.copy()
            if not cv2.countNonZero(umbral): break

        contornos = cv2.findContours(mascara,
                                     cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_NONE)[0]

        valrect = lambda r: r[2] < r[3]
        esrecth = lambda c: valrect(cv2.boundingRect(c))

        numc = np.array([len(contorno) for contorno in contornos])
        mu = numc.mean()
        sigma = numc.std()
        lon = mu + 2.32*sigma

        contornos = [c for c in contornos if lon < len(c) and esrecth(c)]

        if __debug__:
            vi.util.dibujar_rectangulos(baldosa, contornos, 2)
            cv2.imshow('seg_esq1', baldosa)

        if not len(contornos): return None

        # fronteras : x, y, dx, dy
        fronteras = np.array([cv2.boundingRect(c) for c in contornos])
        fronteras[:, 2] += fronteras[:, 0]
        fronteras[:, 3] += fronteras[:, 1]
        ex = -4
        x_min, y_min = fronteras[:, 0].min() - ex, fronteras[:, 1].min() - ex
        x_max, y_max = fronteras[:, 2].max() + ex, fronteras[:, 3].max() + ex

        gris = cv2.cvtColor(baldosa, cv2.COLOR_BGR2GRAY)
        corte = gris[y_min:y_max, x_min:x_max]
        corte = cv2.threshold(corte, 75, 255, cv2.THRESH_BINARY_INV)[1]
        ex = 12
        corte = cv2.copyMakeBorder(corte, ex, ex, ex, ex,
                                   cv2.BORDER_CONSTANT, value=(0, 0, 0))

        dy, dx = corte.shape
        corte = cv2.resize(corte, (int(0.2*dx), int(0.2*dy)))

        if __debug__:
            cv2.imshow('seg_esq2', corte)
            cv2.waitKey()

        return corte
