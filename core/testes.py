import unittest
from .alg_romanos import Numero


class Test_algromanos(unittest.TestCase):

    def test_valores_dos_algarismos_romanos(self):
        n = self.setUp()
        for i in n:
            self.assertAlmostEqual()

    def test_conversao_valor_algarismos_romanos(self):
        a = Numero.roman_to_int(123)
        self.assertEqual(a, "CXXIII")
        b = Numero.roman_to_int(99)
        self.assertEqual(b, "XCIX")
        c = Numero.roman_to_int(9)
        self.assertEqual(c, "IX")
        d = Numero.roman_to_int(4)
        self.assertEqual(d, "IV")

    def test_repeticao_de_algarismos(self):
        d = Numero.roman_to_int(4)
        self.assertEqual(d, "VV")

        print(d)

    def test_tipo_de_input(self):
        a = Numero.roman_to_int("abc")
        self.assertRaises(TypeError, a)




if __name__ == '__main__':
    unittest.main()