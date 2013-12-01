# encoding: utf-8
"""Util """

from random import randint as randz
import numpy as np
import cv2


def __color():
    """Obtener color."""
    return randz(0, 255), randz(0, 255), randz(0, 255)


def dibujar_contornos(imagen, contornos, brocha=1):
    """Dibujar contornos sobre imagen.

    Args:
        imagen (np.array)
            Imagen sobre la que se dibuja los contornos.
        contornos (list)
            Lista de contornos a dibujar.
        brocha (int)
            Número de pixeles de la brocha.
    """
    for contorno in contornos:
        cv2.drawContours(imagen, [contorno], -1, __color(), brocha)


def dibujar_rectangulos(imagen, contornos, brocha=1):
    """Dibujar delimitador rectangular sobre imagen.

    Args:
        imagen (np.array)
            Imagen sobre la que se dibuja los contornos.
        contornos (list)
            Lista de contornos sobre los que calculará el rectángulo.
        brocha (int)
            Número de pixeles de la brocha.
    """
    for x, y, ancho, alto in (cv2.boundingRect(c) for c in contornos):
        cv2.rectangle(imagen, (x, y), (x+ancho, y+alto), __color(), brocha)


def generar_umbrales(imagen, long_bloque, c, long_bloque_p=None, c_p=None):
    """Generar un objeto iterable con distintas imágenes 'umbralizadas'.

    Args:
        imagen
            Imagen base para las imagens 'umbralizadas'.
        long_bloque
            Longitud del bloque para calcular el umbral.
        c
            Constante que se resta al umbral.
        long_bloque_p
            `long_bloque` para generar la siguiente imagen umbralizada.
        c_p
            `c` para generar la siguiente imagen umbralizada.

    Returns:
        Iterable con los contornos.
    """
    if not long_bloque_p:
        long_bloque_p = long_bloque
        c = c_p

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    umbral_1 = cv2.adaptiveThreshold(gris,
                                     255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     long_bloque,
                                     c)
    umbral_2 = cv2.adaptiveThreshold(gris,
                                     255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY,
                                     long_bloque_p,
                                     c_p)

    # Descomentar cuando se crea conveniente
    # if __debug__:
    #     print('- Umbrales')
    #     # int(escala * dimension)
    #     dim = tuple(int(0.7*d) for d in reversed(gris.shape))
    #     cv2.imshow('umbrales',
    #                np.vstack((cv2.resize(umbral_1, dim),
    #                           cv2.resize(umbral_2, dim))))
    #     cv2.waitKey()
    #     cv2.destroyWindow('umbrales')

    return umbral_1, umbral_2


def hallar_contornos(umbrales, modo, metodo):
    """Hallar contornos.

    Args:
        umbrales
            Iterable de imágenes umbralizadas.
        modo
            Modo de recuperación de contornos. Mirar la documentación.
                CV_RETR_EXTERNAL
                CV_RETR_LIST
                CV_RETR_CCOMP
                CV_RETR_TREE
        metodo
            Método de aproximación de contornos. Mirar la documentación.
                CV_CHAIN_APPROX_NONE
                CV_CHAIN_APPROX_SIMPLE
                CV_CHAIN_APPROX_TC89_L1, CV_CHAIN_APPROX_TC89_KCOS
    Returns:
        Lista de contornos.
    """
    mezcla = [cv2.findContours(umbral, modo, metodo)[0]
              for umbral in umbrales]
    return [contorno for contornos in mezcla for contorno in contornos]
