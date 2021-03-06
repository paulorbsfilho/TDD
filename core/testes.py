import unittest

from .alg_romanos import Numero

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

    # noinspection PyCallByClass
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

    def test_repeticao_algarism_I(self):
        try:
            a = Numero.roman_to_int('IIII')
        except ValueError:
            print (u"Este algarismo só pode ser repetido 3 vezes!: I")

    def test_repeticao_algarismo_V(self):
        try:
            a = Numero.roman_to_int('VV')
        except ValueError:
            print(u"Este algarismo não pode ser repetido!: V")

    def test_repeticao_algarismo_X(self):
        try:
            a = Numero.roman_to_int('XXXX')
        except ValueError:
            print(u"Este algarismo só pode ser repetido 3 vezes!: X")

    def test_repeticao_algarismo_L(self):
        try:
            a = Numero.roman_to_int('LL')
        except ValueError:
            print(u"Este algarismo não pode ser repetido!: L")

    def test_repeticao_algarismo_C(self):
        try:
            a = Numero.roman_to_int('CCCC')
        except ValueError:
            print(u"Este algarismo só pode ser repetido 3 vezes!: C")

    def test_repeticao_algarismo_D(self):
        try:
            a = Numero.roman_to_int('DD')
        except ValueError:
            print(u"Este algarismo não pode ser repetido!: D")

    def test_repeticao_algarismo_M(self):
        try:
            a = Numero.roman_to_int('MMMM')
        except ValueError:
            print(u"Este algarismo só pode ser repetido 3 vezes!: M")

    def test_ordem_dos_algarismos(self):
        ar = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        a = "LMX"
        maior = 0
        menor = 0
        r = ""
        try:
            for i in a:
                if ar[i] > menor:
                    r = r + i
                    menor = maior
                    maior = ar[i]
                    if menor != 0:
                        if maior*0.1 == menor or menor*5 == maior:
                            pass
                        else:
                            r = r[-2::]
                            raise ValueError
        except ValueError:
            print(u"A ordem dos algarismos é inválida: %s" %(r))

    def test_conversao_automatico(self):
        a = Numero.converter(12)
        self.assertEqual(a, "XII")
        b = Numero.converter("XII")
        self.assertEqual(b, 12)

    def test_input_vazio(self):
        try:
            a = Numero.converter("")
        except ValueError:
            print(u"Entrada vazia. Você não inseriu numeros romanos ou inteiros")


if __name__ == '__main__':
    unittest.main()