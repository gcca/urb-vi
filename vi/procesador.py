#!/usr/bin/python
# encoding: utf-8
"""
vi.procesador -- brief

La variable `procesos` mantiene el orden de lo métodos empleados: captura,

"""
from __future__ import unicode_literals, print_function

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
        for proceso in PROCESOS:
            resultado = proceso.ejecutar(resultado)
    except ValueError as err:
        raise SystemExit('\nMódulo '
                         + str(type(proceso))
                         + ' recibió parámetro incorreco: '
                         + err.message)
    else:
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
        try:
            modulo = importlib.import_module(
                'vi.metodo.' + nombre + '.' + metodo)
        except ImportError as e:
            print('Error al importar: %s.%s: %s' % (nombre, metodo, e.message))
            import sys
            sys.exit(-1)
        metodo_clase = getattr(modulo, nombre.capitalize())
        metodo_instancia = metodo_clase()
        PROCESOS.append(metodo_instancia)
