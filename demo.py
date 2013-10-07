#!/usr/bin/python
# encoding: utf-8
"""
Ejecutar demo
"""
import sys
import importlib

def inicio(ruta):
    """Recibe la ruta del módulo que contiene la demo """
    modulo = importlib.import_module('demo.' + ruta)
    modulo.demo()

if '__main__' == __name__:
    inicio(sys.argv[1])
