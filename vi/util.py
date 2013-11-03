# encoding: utf-8
"""Util """

import cv2

colors = [
    (255,   0,   0),
    (  0, 255,   0),
    (  0,   0, 255),
    (255, 255,   0),
    (  0, 255, 255),
    (255,   0, 255),
    (255, 255, 255),
    (200, 140,   0),
    (255,  10, 100),
]

def dibujar_contornos(imagen, contornos):
    """Dibujar contornos sobre imagen.

    Args:
        imagen (np.array)
            Imagen sobre la que se dibuja los contornos.
        contornos (list)
            Lista de contornos a dibujar.
    """
    # cv2.drawContours(image, contours, -1, colors[0], 2)
    i = 0
    for c in contornos:
        color = colors[i]
        i += 1
        if len(colors) == i: i = 0
        cv2.drawContours(imagen, [c], -1, color, 2)

def dibujar_rectangulos(imagen, contornos):
    """Dibujar delimitador rectangular sobre imagen.

    Args:
        imagen (np.array)
            Imagen sobre la que se dibuja los contornos.
        contornos (list)
            Lista de contornos sobre los que calculará el rectángulo.
    """
    # cv2.drawContours(image, contours, -1, colors[0], 2)
    i = 0
    for x, y, dx, dy in contornos:
        color = colors[i]
        i += 1
        if len(colors) == i: i = 0
        cv2.rectangle(imagen, (x, y), (x+dx, y+dy), color, 2)
