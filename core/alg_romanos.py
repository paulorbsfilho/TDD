class Numero():

    def int_to_roman(a):
        if not isinstance(a, type(1)):
            raise TypeError("expected integer, got %s" % type(a))
        if not 0 < a < 4000:
            raise ValueError("Argument must be between 1 and 3999")
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []

        for i in range(len(ints)):
            count = int(a / ints[i])
            result.append(nums[i] * count)
            a -= ints[i] * count
        return ''.join(result)

    def roman_to_int(a):
        if not isinstance(a, type("")):
            raise TypeError("expected string, got %s" % type(a))
        a = a.upper()
        nums = {'M': 1000,
                'D': 500,
                'C': 100,
                'L': 50,
                'X': 10,
                'V': 5,
                'I': 1}
        sum = 0
        for i in range(len(a)):
            try:
                value = nums[a[i]]
                if i + 1 < len(a) and nums[a[i + 1]] > value:
                    sum -= value
                else:
                    sum += value
            except KeyError:
                raise ValueError('a is not a valid Roman numeral: %s' % a)

        if Numero.int_to_roman(sum) == a:
            return sum
        else:
            raise ValueError('a is not a valid Roman numeral: %s' % a)


class Conversor():

    def converter(self,a):
        if type(a)==type(1):
            r = Numero()
            return r.int_to_roman(a)
        elif type(a)==type(""):
            n = Numero()
            return n.roman_to_int(a)
        else:
            raise TypeError("expected integer, got %s" % type(a))


def main():
    print("Digite um numero em algarismos romamos")
    #a = a()
    n = Numero.roman_to_int("xx")
    print(n)
    print("Digite um numero inteiro")
    #b = int(a())
    r = Numero.int_to_roman(99)
    print(r)
    # t = Conversor.converter(12)
    # print(t)
    # v = Conversor.converter("MMXVIII")
    # print(v)


if __name__ == '__main__':
    main()