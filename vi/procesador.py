#!/usr/bin/python
# encoding: utf-8
"""
vi.procesador -- brief

La variable `procesos` mantiene el orden de lo métodos empleados: captura,

"""
from __future__ import unicode_literals, print_function

import sys
import os
import importlib

PROCESOS = []

def ejecutar(resultado=None):
    """(object) -> NoneType
    Args:
        resulado -- Primer parámetro de proceso

    Excepciones:
     - Lanzar `ValueError` cuando existen excepciones por haber recibido
       un mal parámetro.
     - Cualquier otra excepción debida a la implementación debe ir solo
       como `Exception` o alguna otra afín.
    """
    assert PROCESOS, 'Invocar antes la función `iniciar(args)`'
    try:
        devnull = open(os.devnull, 'w')
        fdnul = devnull.fileno()
        fdout = sys.stdout.fileno()
        fderr = sys.stderr.fileno()
        dupfdout = os.dup(fdout)
        dupfderr = os.dup(fderr)
        os.dup2(fdnul, fdout)
        os.dup2(fdnul, fderr)
        for proceso in PROCESOS:
            resultado = proceso.ejecutar(resultado)
    except ValueError as err:
        raise SystemExit('\nMódulo '
                           + str(type(proceso))
                           + ' recibió parámetro incorreco: '
                           + err.message)
    except Exception as err:
        raise SystemExit('\nMódulo '
                           + str(type(proceso))
                           + ' error: '
                           + err.message)
    else:
        sys.stdout.flush()
        sys.stderr.flush()
        os.dup2(dupfdout, fdout)
        os.dup2(dupfderr, fderr)
        return resultado

def iniciar(args):
    """() -> NoneType

    Recaba las clase definidas en `args`

    'fichero'    Imagen         Imagen            Arreglo            Placas
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
    for nombre in ['captura', 'deteccion', 'segmentacion', 'reconocimiento']:
        metodo = getattr(args, 'met_' + nombre)
        modulo = importlib.import_module('vi.metodo.' + nombre + '.' + metodo)
        metodo_clase = getattr(modulo, nombre.capitalize())
        metodo_instancia = metodo_clase()
        PROCESOS.append(metodo_instancia)
