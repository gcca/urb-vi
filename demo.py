#!/usr/bin/python

import sys
import importlib

def inicio(ruta):
    modulo = importlib.import_module('demo.' + ruta)
    modulo.demo()

if '__main__' == __name__:
    inicio(sys.argv[1])
