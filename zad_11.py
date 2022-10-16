#Paweł Majewski EiT Programowanie w języku Python
#zad_11
def matrix_multiplication(a, b):
    c = 0
    if len(a) == len(b):
        for i in range(0, len(a)):
            c += a[i] * b[i]
        print(c)
    else:
        print("zly rozmiar")


if __name__ == '__main__':

    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]

    matrix_multiplication(a,b)
