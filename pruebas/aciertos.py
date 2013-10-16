#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Prueba que ejecuta la aplicación por cada imagen y verifica si la placa
fue leída correctamente.
"""
from __future__ import print_function

import sys
sys.path.append('..')
sys.path.append('.')

import os
import argparse
import csv
import vi.procesador
import mock

devnull = open(os.devnull, 'w')
fdnul = devnull.fileno()

def dicc_imagen_placas(ruta_csv):
    """Diccionario de placas por imagen
    >>> dicc_imagen_placas('../recursos/img.csv')
    {
        '1': ['AB666'],
        '30': ['OPA898'],
        ...
    }
    """
    with open(ruta_csv) as fich_csv:
        placas_csv = csv.reader(fich_csv)
        placas_x_imagen = { fila[0]: fila[1:] for fila in placas_csv }
    return placas_x_imagen

def contador_aciertos(ruta_imagenes):
    """
    - Obtiene la lista de imágenes y placas.
    - Aplica el análisis por imagen.
    - Compara placas.
    """
    ruta_recursos = os.path.dirname(ruta_imagenes)
    ruta_csv = os.path.join(ruta_recursos, 'img.csv')

    placas_x_imagen = dicc_imagen_placas(ruta_csv)

    if __debug__: prints = []

    colector = []

    fdout = sys.stdout.fileno()
    fderr = sys.stderr.fileno()
    dfdout = os.dup(fdout)
    dfderr = os.dup(fderr)
    os.dup2(fdnul, fdout)
    os.dup2(fdnul, fderr)

    for nombre_imagen, placas_esperadas in placas_x_imagen.items():
        ruta_imagen = os.path.join(ruta_imagenes, nombre_imagen + '.png')
        placas_obtenidas = vi.procesador.ejecutar(ruta_imagen)
        obtenidas = placas_obtenidas
        esperadas = placas_esperadas
        colector.append(any((obtenida in esperadas) for obtenida in obtenidas))

        if __debug__:
            prints.append((nombre_imagen, placas_obtenidas))

    sys.stdout.flush()
    sys.stderr.flush()
    os.dup2(dfdout, fdout)
    os.dup2(dfderr, fderr)

    cantidad_aciertos = sum(colector)
    cantidad_errores = len(colector) - cantidad_aciertos

    if __debug__:
        for p in prints:
            print('Imagen %s: %s' % p)

    print('Cantidad de aciertos: %s' % cantidad_aciertos)
    print('Cantidad de errores: %s' % cantidad_errores)

def inicio():
    """Inicio de ejecución """
    parser = argparse.ArgumentParser()
    parser.add_argument('ruta_imagenes')
    args = parser.parse_args()
    assert not args.ruta_imagenes is None, 'Sin ruta a las imágenes'
    procesador_args = mock.Mock(met_captura='babas',
                                met_deteccion='babas',
                                met_segmentacion='contorno2',
                                met_reconocimiento='tesseractOCR')
    vi.procesador.iniciar(procesador_args)
    contador_aciertos(args.ruta_imagenes)

if '__main__' == __name__:
    inicio()
