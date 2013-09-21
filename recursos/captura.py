#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""
Captura de imágenes de muestra
"""

import os
import argparse
import cv2
import Tkinter
import tkSimpleDialog


def var_estt(var_nom, val):
    """Crear variable estática """
    def funda(func):
        """Funda """
        setattr(func, var_nom, val)
        return func
    return funda


@var_estt('val', 100)
def intervalo(val):
    """Actualizar intervalo de video """
    intervalo.val = val

@var_estt('cont', 0)
@var_estt('fich', None)
def imagen_guardar(img, dst_dir):
    """Guardar imagen en secuencia  """
    cont = str(imagen_guardar.cont)
    dst = os.path.join(dst_dir, cont) + '.png'
    placa = tkSimpleDialog.askstring('Ingreso de placa', 'Placa:')

    cv2.imwrite(dst, img, [cv2.cv.CV_IMWRITE_PNG_COMPRESSION, 0])
    imagen_guardar.fich.write('%s,%s\n' % (cont, placa))
    imagen_guardar.cont += 1

def contexto_inic(local_args):
    """Inicializar las variables de contexto """
    fich = os.path.join(local_args.dir, 'placas.csv')

    Tkinter.Tk().withdraw()
    imagen_guardar.cont = int(local_args.cont_i)
    imagen_guardar.fich = open(fich, 'w')

def contexto_fin():
    """Finalizar las variables de contexto """
    imagen_guardar.fich.close()

def captura(video_ruta, destino_dir):
    """Ciclo de captura """
    assert '' != video_ruta
    assert '' != destino_dir
    assert not imagen_guardar.fich is None

    pausa = False

    cam = cv2.VideoCapture(video_ruta)
    _, img = cam.read()

    while True:
        tecla = 0xff & cv2.waitKey(intervalo.val)

        if 97 == tecla:
            imagen_guardar(img, destino_dir)

        if 27 == tecla:
            break

        if 32 == tecla:
            pausa = not pausa

        if pausa:
            continue

        _, img = cam.read()

        cv2.imshow('ven1', img)

    cv2.destroyAllWindows()


def inic():
    """Inicio de ejecución """
    parser = argparse.ArgumentParser(
        description=u'Captura de imágenes de muestra',
        epilog=u'[A] Capturar - [:SPACE:] Pausa - [:ESC:] Salir')

    parser.add_argument('--video',
                        help='Ruta al fichero de video',
                        required=True)
    parser.add_argument('--dir',
                        help=u'Directorio de destino de las imágenes',
                        required=True)
    parser.add_argument('--cont_i',
                        help='Valor inicial del contador',
                        required=True)

    args = parser.parse_args()

    assert os.path.exists(args.dir), 'No existe el directorio ' + args.dir
    assert args.cont_i.isdigit(), '`cont_i` debe ser un número'

    contexto_inic(args)
    captura(args.video, args.dir)
    contexto_fin()

if __name__ == '__main__':
    inic()
