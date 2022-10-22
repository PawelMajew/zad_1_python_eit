#Paweł Majewski EiT Programowanie w języku Python
#zad_15
# Zdefiniuj klasę reprezentującą liczby zespolone
# (wraz z funkcjami na nich działającymi np. dodawanie, odejmowanie itd.)
import math
from math import sqrt


class MyComplex(object):

    def __init__(self, real, imag = 0.0):
        self.real = real
        self.imag = imag
        # Formats our results
        print(self.real + self.imag)

    def __add__(self, other):
        print('\nSum:')
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        print('\nDifference:')
        return MyComplex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        print('\nProduct:')
        return MyComplex((self.real * other.real) + (self.imag * other.imag),
                         (self.imag * other.real) + (self.real * other.imag))

    def __truediv__(self, other):
        print('\nQuotient:')
        return MyComplex(((self.real+self.imag) * (other.real-other.imag)) /
                         ((other.real+other.imag) * (other.real-other.imag)))

    def abs(self):
        print('\nAbsolute Value:')
        new = (self.real**2 + (self.imag**2) * -1)
        return MyComplex(sqrt(new.real))


if __name__ == '__main__':
    i = MyComplex(2, 10j)
    k = MyComplex(3, 5j)

    i + k
    i - k
    i * k
    i / k
    MyComplex.abs(i)
    MyComplex.abs(k)
