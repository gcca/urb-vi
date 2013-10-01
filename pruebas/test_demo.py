import unittest2
import vi.procesador

class TestDemo(unittest2.TestCase):

    def test_retrollamadas(self):
        """Resultado de llamadas sucesivas. """

        class Args:
            def __init__(self):
                self.met_captura = 'demo'
                self.met_deteccion = 'demo'
                self.met_segmentacion = 'demo'
                self.met_reconocimiento = 'demo'

        args = Args()

        vi.procesador.inic(args)
        actual = vi.procesador.ejecutar('inicio ')

        esperado = 'inicio captura deteccion segmentacion reconocimiento'

        self.assertEqual(actual, esperado)
