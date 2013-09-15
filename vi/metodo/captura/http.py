# -*- coding: utf-8 -*-

'''
Método Http
'''

from urllib2 import urlopen
from PIL import Image
from cStringIO import StringIO
import numpy as np


class Captura(object):
    '''
    Captura Http
    '''

    def __init__(self, url):
        try:
            self.fuente = urlopen(url)
        except IOError:
            raise AttributeError


    def ejecutar(self, *args):
        '''
        Args:
            url - URL de la imagen

        Rets:
            La imagen en formato JPG
        '''

        fuente = self.fuente

        constructor = []

        for tarugo in fuente:
            # \r\n
            if 2 == len(tarugo):
                break

        for tarugo in fuente:
            if '--myb' in tarugo:
                break
            constructor.append(tarugo)

        io = ''.join(constructor)
        img = StringIO(io)
        try:
            img = Image.open(img).convert('RGB')
        except IOError:
            # IMLPEMENTAR SISTEMA DE LOGGING
            # Este tipo de errores son propios de los cambios que se dan
            # al hacer uso de una biblioteca que no se conoce
            # su sistema de excepciones. Mejora el mantenimiento.
            raise IOError('Decodificador JPG')
        except:
            return np.array()

        img = np.array(img)

        return img
