# encoding: utf-8

"""Segmetación por búsqueda de contornos """

from __future__ import division

import cv2
import numpy as np

class Segmentacion(object):
    """Segmentación con filtro por área media """

    def __init__(self):
        """Agrega el procesador """
        super(Segmentacion, self).__init__()
        self._procesadores = [self.procesador_areamedia]

    def ejecutar(self, baldosas):
        """Recibe una lista de baldosas para ser pre-procesadas y mejorar
        la lectura de los caracteres. Retorna la lista de baldosas procesadas.
        """
        out = [self._procesar(baldosa) for baldosa in baldosas]        
        out2 = []
        for letras in out:
            if len(letras)>4:
                out2.append(letras)
                
        return out2
    
    def _procesar(self, baldosa):
        """Aplica los pre-procesadores a la baldosa. """
        procesada = baldosa
        for procesador in self._procesadores:
            procesada = procesador(procesada)
        return procesada
    
    @staticmethod
    def procesador_areamedia(baldosa):
        """En base al promedio, retira elementos que podrían no ser letras """
        gris = cv2.cvtColor(baldosa, cv2.COLOR_BGR2GRAY)
        _, binarizado = cv2.threshold(gris, 90, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(binarizado,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

        areas = [cv2.contourArea(c) for c in contornos]
        d_areas =  np.array(areas)
        mu = d_areas.mean()
        sigma = d_areas.std()

        filtrados = []
        for contorno, area in zip(contornos, areas):
            if 50 < area < mu - 0.05*sigma:
                filtrados.append(contorno)        

        marcos = []
        if len(filtrados)>4:
            regiones = [cv2.boundingRect(contorno) for contorno in filtrados] 
            _, binarizado = cv2.threshold(gris, 90, 255, 
                                          cv2.THRESH_BINARY_INV)            
            letras = [binarizado[y:(y+dy), x:(x+dx)] 
                      for x, y, dx, dy in regiones] 
            for letra in letras:
                zoom = cv2.resize(letra, (100, 100))
                marcos.append(zoom)
        return marcos   
