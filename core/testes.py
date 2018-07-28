import unittest

from .alg_romanos import Numero, Conversor

class Test_algromanos(unittest.TestCase):

    def test_conversao_valor_algarismos_romanos(self):
        a = Numero.int_to_roman(1)
        self.assertEqual(a, 'I')
        b = Numero.int_to_roman(5)
        self.assertEqual(b, 'V')
        c = Numero.int_to_roman(10)
        self.assertEqual(c, 'X')
        d = Numero.int_to_roman(50)
        self.assertEqual(d, 'L')
        d = Numero.int_to_roman(100)
        self.assertEqual(d, 'C')
        d = Numero.int_to_roman(500)
        self.assertEqual(d, 'D')
        d = Numero.int_to_roman(1000)
        self.assertEqual(d, 'M')


if __name__ == '__main__':
    unittest.main()