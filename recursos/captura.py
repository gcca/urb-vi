# -*- coding: utf-8 -*-

"""
Captura de imágenes de muestra
"""

import os
import argparse
import cv2


def var_estatica(var_nom, val):
    """Crear variable estática """
    def funda(func):
        """Funda """
        setattr(func, var_nom, val)
        return func
    return funda


@var_estatica('val', 100)
def intervalo(val):
    """Actualizar intervalo de video """
    intervalo.val = val

@var_estatica('cont', 0)
def imagen_guardar(img, dst_dir):
    """Guardar imagen en secuencia  """
    dst = os.path.join(dst_dir, str(imagen_guardar.cont)) + '.png'
    cv2.imwrite(dst, img, [cv2.cv.CV_IMWRITE_PNG_COMPRESSION, 0])
    imagen_guardar.cont += 1

def contexto_inic(local_args):
    """Inicializar las variables de contexto """
    imagen_guardar.cont = int(local_args.cont_i)

def captura(video_ruta, destino_dir):
    """Ciclo de captura """
    assert '' != video_ruta
    assert '' != destino_dir

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
        epilog='[A] Capturar <-> [:SPACE:] Pausa <-> [:ESC:] Salir')

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

    assert os.path.exists(args.dir), 'No existe el directorio'
    assert args.cont_i.isdigit(), '`cont_i` debe ser un número'

    contexto_inic(args)

    captura(args.video, args.dir)

if __name__ == '__main__':
    inic()
