# encoding: utf-8
"""Util """

from random import randint as randz
import cv2


def __color():
    """Obtener color."""
    return randz(0, 255), randz(0, 255), randz(0, 255)


def dibujar_contornos(imagen, contornos):
    """Dibujar contornos sobre imagen.

    Args:
        imagen (np.array)
            Imagen sobre la que se dibuja los contornos.
        contornos (list)
            Lista de contornos a dibujar.
    """
    for contorno in contornos:
        cv2.drawContours(imagen, [contorno], -1, __color(), 2)


def dibujar_rectangulos(imagen, contornos):
    """Dibujar delimitador rectangular sobre imagen.

    Args:
        imagen (np.array)
            Imagen sobre la que se dibuja los contornos.
        contornos (list)
            Lista de contornos sobre los que calculará el rectángulo.
    """
    for x, y, ancho, alto in contornos:
        cv2.rectangle(imagen, (x, y), (x+ancho, y+alto), __color(), 2)
