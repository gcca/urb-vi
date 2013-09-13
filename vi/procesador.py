#!/usr/local/bin/python2.7
# encoding: utf-8
"""
vi.procesador -- brief
"""

import importlib

procesos = []

def ejecutar(resultado=None):
    """() -> NoneType """

    for proceso in procesos:
        resultado = proceso.ejecutar(resultado)

    return resultado

def inic(args):
    for nombre in ['captura', 'deteccion', 'segmentacion', 'extraccion']:
        metodo = getattr(args, 'met_' + nombre)
        modulo = importlib.import_module('vi.metodo.' + nombre + '.' + metodo)
        Metodo = getattr(modulo, metodo.capitalize())
        instanciaMetodo = Metodo()
        procesos.append(instanciaMetodo)