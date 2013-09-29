#!/usr/local/bin/python2.7
# encoding: utf-8
"""
vi.procesador -- brief

La variable `procesos` mantiene el orden de lo métodos empleados: captura,

"""

import importlib

procesos = []

def ejecutar(resultado=None):
    """(object) -> NoneType

    Primer parámetro de proceso
    """

    for proceso in procesos:
        resultado = proceso.ejecutar(resultado)

    return resultado

def inic(args):
    """() -> NoneType

    Recaba las clase definidas en `args`

    'fichero'    Imagen         Imagen           Arreglo             Placas
       +---------+  +-----------+  +--------------+  +----------------+
     o-| Captura |->| Deteccion |->| Segmentacion |->| Reconocimiento |-@
       +---------+  +-----------+  +--------------+  +----------------+

    Args:
        args - Objeto con atributos de los métodos
        >>> args.met_captura = 'demo'
        >>> args.met_deteccion = 'demo'
        >>> args.met_segmentacion = 'demo'
        >>> args.met_reconocimiento = 'demo'
    """
    for nombre in ['captura', 'deteccion', 'segmentacion', 'extraccion']:
        metodo = getattr(args, 'met_' + nombre)
        modulo = importlib.import_module('vi.metodo.' + nombre + '.' + metodo)
        Metodo = getattr(modulo, metodo.capitalize())
        instanciaMetodo = Metodo()
        procesos.append(instanciaMetodo)
