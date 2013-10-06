"""Prueba demo """

import unittest2
import mock
import vi.procesador

class TestDemo(unittest2.TestCase):
    """Prueba demo """

    def test_retrollamadas(self):
        """Resultado de llamadas sucesivas. """
        args = mock.Mock(met_captura = 'demo',
                         met_deteccion = 'demo',
                         met_segmentacion = 'demo',
                         met_reconocimiento = 'demo')
        vi.procesador.iniciar(args)
        actual = vi.procesador.ejecutar('inicio ')

        esperado = 'inicio captura deteccion segmentacion reconocimiento'

        self.assertEqual(actual, esperado)
