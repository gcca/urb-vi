# -*- coding: utf-8 -*-

"""Segmetación por búsqueda de contornos """

import cv2

class Segmentacion(object):
    """Segmentación por contornos """

    def __init__(self):
        """Inicia la lista de filtros """
        self.filtros = [self.filtro_numPixeles]

    def ejecutar(self, imagen):
        """Recibe una imagen y retorna una lista con las secciones limitadas
        por los contornos """
        imgris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        _, umbral = cv2.threshold(imgris, 100, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(umbral,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_NONE)

        filtrados = []
        for contorno in contornos:
            # (-o-)
            # Implementación temporal
            # -> Validar en cascada
            if all(self.validar(contorno)):
                filtrados.append(contorno)

        regiones = [cv2.boundingRect(contorno) for contorno in filtrados]
        baldosas = [imagen[y:y + dy, x:x + dx] for x, y, dx, dy in regiones]

        return baldosas

    def validar(self, contorno):
        """Devuelve un generador con valores booleanos por cada filtro

        >>> # Si hubieran dos filtros y el segundo falla
        >>> list(self.validar(contorno))
        [True, False]
        """
        return (bool(filtrar(contorno)) for filtrar in self.filtros)

    def filtro_numPixeles(self, contorno):
        """Filtro simple
        No considerar como válido porque solo aplica a la imagen de la demo
        """
        return 200 < len(contorno)
