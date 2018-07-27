import unittest
from .alg_romanos import Numero


class Test_algromanos(unittest.TestCase):

    def test_valores_dos_algarismos_romanos(self):
        i = Numero.romano_para_int(1)
        self.assertEqual(i, "I")
        v = Numero.romano_para_int(5)
        self.assertEqual(v, "V")
        x = Numero.romano_para_int(10)
        self.assertEqual(x, "X")
        l = Numero.romano_para_int(50)
        self.assertEqual(l, "L")
        c = Numero.romano_para_int(100)
        self.assertEqual(c, "C")
        d = Numero.romano_para_int(500)
        self.assertEqual(d, "D")
        m = Numero.romano_para_int(1000)
        self.assertEqual(m, "M")

    def test_conversao_valor_algarismos_romanos(self):
        a = Numero.romano_para_int(123)
        self.assertEqual(a, "CXXIII")
        b = Numero.romano_para_int(99)
        self.assertEqual(b, "XCIX")
        c = Numero.romano_para_int(9)
        self.assertEqual(c, "IX")
        d = Numero.romano_para_int(4)
        self.assertEqual(d, "IV")

    def test_repeticao_de_algarismos(self):
        d = Numero.romano_para_int(4)
        self.assertEqual(d, "IV")
        print(d)

if __name__ == '__main__':
    unittest.main()