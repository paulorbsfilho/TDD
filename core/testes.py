import unittest

from .alg_romanos import Numero, Conversor

class Test_algromanos(unittest.TestCase):

    def test_conversao_de_valores_interiros_para_romano(self):
        a = Numero.int_to_roman(1)
        self.assertEqual(a, 'I')
        b = Numero.int_to_roman(5)
        self.assertEqual(b, 'V')
        c = Numero.int_to_roman(10)
        self.assertEqual(c, 'X')
        d = Numero.int_to_roman(50)
        self.assertEqual(d, 'L')
        e = Numero.int_to_roman(100)
        self.assertEqual(e, 'C')
        f = Numero.int_to_roman(500)
        self.assertEqual(f, 'D')
        g = Numero.int_to_roman(1000)
        self.assertEqual(g, 'M')

    def test_conversao_valor_algarismos_romanos(self):
        a = Numero.roman_to_int('I')
        self.assertEqual(a, 1)
        b = Numero.roman_to_int('V')
        self.assertEqual(b, 5)
        c = Numero.roman_to_int('X')
        self.assertEqual(c, 10)
        d = Numero.roman_to_int('L')
        self.assertEqual(d, 50)
        e = Numero.roman_to_int('C')
        self.assertEqual(e, 100)
        f = Numero.roman_to_int('D')
        self.assertEqual(f, 500)
        g = Numero.roman_to_int('M')
        self.assertEqual(g, 1000)

if __name__ == '__main__':
    unittest.main()