# encoding: utf-8

"""Módulo principal."""

from collections import namedtuple

from PyQt4 import uic
from PyQt4.QtGui import QMainWindow, QFileDialog

import vi.procesador


class GVi(QMainWindow):
    """Ventana principal."""

    def __init__(self):
        super(GVi, self).__init__()
        uic.loadUi('gvi/gvi_principal.ui', self)

        Args = namedtuple('Args',
                          'met_captura '
                          'met_deteccion '
                          'met_segmentacion '
                          'met_reconocimiento')
        vi.procesador.iniciar(Args('babas', 'contorno', 'esqueleto', 'tessi'))

        self.barAvance.setValue(100)

        self.btnAbrir.clicked.connect(self.btnAbrir_clic)
        self.btnProcesar.clicked.connect(self.btnProcesar_clic)

    def btnAbrir_clic(self):
        """Evento: seleccionar imagen."""
        imagen_ruta = QFileDialog.getOpenFileName(self, 'Abrir imagen')
        self.edRuta.setText(imagen_ruta)

    def btnProcesar_clic(self):
        """Evento: procesar imagen."""
        lista = str(self.edRuta.text())  # ruta de la imagen

        i = 25
        self.barAvance.setValue(0)
        for proceso in vi.procesador.PROCESOS:
            lista = proceso.ejecutar(lista)
            self.barAvance.setValue(i)
            i += 25

        for placa in {p for p in lista if p}:
            self.lsPlacas.insertItem(0, placa)
