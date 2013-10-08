#!/usr/bin/python
# encoding: utf-8

"""
Urb Vi - Visor de placas
"""

import argparse
import textwrap

import vi.procesador

def urbvi():
    """Hilo de ejecución principal """
    parser = argparse.ArgumentParser(description=textwrap.dedent('''
    Urb - Vi Visor de Placas

    Autores:
        - César Cárdenas
        - Cristhian Gonzales
        - César Salazar
    '''), formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--met_captura',
                        metavar='CAPTURA',
                        help='Nombre del método de captura.')
    parser.add_argument('--met_deteccion',
                        metavar='DETECCION',
                        help='Nombre del método de detección.')
    parser.add_argument('--met_segmentacion',
                        metavar='SEGMENTACION',
                        help='Nombre del método de segmentación.')
    parser.add_argument('--met_reconocimiento',
                        metavar='RECONOCIMIENTO',
                        help='Nombre del método de reconocimiento.')
    parser.add_argument('--param',
                        metavar='PARAMETRO',
                        help='Parámetro inicial. Ruta a la imagen.')
    args = parser.parse_args()

    # Inicio del proceso
    vi.procesador.iniciar(args)
    resultado = vi.procesador.ejecutar(args.param)
    print(resultado)

if '__main__' == __name__:
    urbvi()
