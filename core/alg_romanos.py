class Numero():

    def romano_para_int(a):
        rom = ""
        while a >= 1000:
            rom = rom + 'M'
            a = a - 1000
        while a >= 500:
            rom = rom + 'D'
            a = a - 500
        while a >= 100:
            rom = rom + 'C'
            a = a - 100
        while a >= 50:
            rom = rom + 'L'
            a = a - 50
        while a >= 10:
            rom = rom + 'X'
            a = a - 10
        while a >= 5:
            rom = rom + 'V'
            a = a - 5
        while a >= 1:
            rom = rom + 'I'
            a = a - 1
        return rom

    def rom_para_int(a):
        pass



def main():
    print("Digite um numero em algarismos romamos")
    a = int(input())
    n = Numero.romano_para_int(a)
    print(n)


if __name__ == '__main__':
    main()