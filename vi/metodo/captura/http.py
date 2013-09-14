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

    def ejecutar(self, url):
        '''
        Args:
            url - URL de la imagen

        Rets:
            La imagen en formato JPG
        '''
        try:
            fuente = urlopen(url)
        except IOError:
            raise AttributeError
        else:
            n = ''
            for _ in xrange(3):
                fuente.readline()

            for a in fuente:
                if '--myb' in a:
                    break
                n += a

            im = StringIO(n)
            try:
                im = Image.open(im).convert('RGB')
            except IOError:
                # IMLPEMENTAR SISTEMA DE LOGGING
                # Este tipo de errores son propios de los cambios que se dan
                # al hacer uso de una biblioteca que no se conoce
                # su sistema de excepciones. Mejora el mantenimiento.
                raise IOError('Decodificador JPG')
            except:
                return self.prev

            im = np.array(im)

            return im
