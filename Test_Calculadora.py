import unittest
from Calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(0, 7), -7)
        self.assertEqual(restar(-3, -2), -1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(-1, 5), -5)
        self.assertEqual(multiplicar(0, 100), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)

    def test_dividir_por_cero(self):
        self.assertEqual(dividir(10, 0), "Error: Division por cero")

if __name__ == "__main__":
    unittest.main()
