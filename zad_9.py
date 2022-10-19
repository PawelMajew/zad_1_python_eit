#Paweł Majewski EiT Programowanie w języku Python
#zad_9
# Napisz skrypt obliczający pierwiastki równania kwadratowego
# w postaci : y = ax2+bx+c. Wejściem skryptu są wartości: a, b, c

import math


def get_value():
    return input("podaj wartosci rownania a, b, c\n")


def quadratic_equation(abc):
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(abc)
    if a == 0:
        print("to nie jest rownanie kwadratowe\n")
    if a != 0:
        delta = b * b - 4 * a * c

        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(x1,x2)

        if delta < 0:
            print("brak rozwiazania\n")

        if delta == 0:
            x1 = -b / (2 * a)
            print(x1)


def engine():
    while 1:
        try:
            temp = get_value()
            quadratic_equation(temp.split())
            break
        except ValueError:
            print("zle wartosci jeszcze raz\n")


if __name__ == '__main__':

    engine()

