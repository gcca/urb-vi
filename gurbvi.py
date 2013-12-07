#!/usr/bin/python2
# encoding: utf-8

"""Interfaz Gráfica."""

import sys
from PyQt4.QtGui import QApplication
from gvi.gvi import GVi


def gvi_inicio():
    """Inicio."""
    aplic = QApplication(sys.argv)
    gvi_principal = GVi()
    gvi_principal.show()
    sys.exit(aplic.exec_())


if '__main__' == __name__:
    gvi_inicio()
