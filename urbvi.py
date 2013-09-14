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
    parser.add_argument('--met_extraccion',
                        metavar='EXTRACCION',
                        help='Nombre del método de extracción.')
    args = parser.parse_args()

    # Inicio del proceso
    vi.procesador.inic(args)
    resultado = vi.procesador.ejecutar()
    print(resultado)

if '__main__' == __name__:
    urbvi()
