# -*- coding: utf-8 -*-
"""Prueba demo """

import unittest2
import mock
import vi.procesador

class TestDemo(unittest2.TestCase):
    """Prueba demo """

    def setUp(self):
        """Limpia la lista de procesos antes de cada método de prueba """
        vi.procesador.PROCESOS = []

    def test_retrollamadas(self):
        """Resultado de llamadas sucesivas. """
        args = mock.Mock(met_captura='demo',
                         met_deteccion='demo',
                         met_segmentacion='demo',
                         met_reconocimiento='demo')
        vi.procesador.iniciar(args)
        actual = vi.procesador.ejecutar('inicio ')

        esperado = 'inicio captura deteccion segmentacion reconocimiento'

        self.assertEqual(actual, esperado)

    def test_sin_iniciar(self):
        """AssertionError si no se invoca a `iniciar` """
        self.assertRaises(AssertionError, vi.procesador.ejecutar)

if '__main__' == __name__:
    unittest2.main()
