#Paweł Majewski EiT Programowanie w języku Python
#zad_16
# Wykorzystaj powyzszą klasę do stworzenia prostego kalkulatora, parsującego i wykonującego równanie podane przez
# użytkownika
from zad_15 import MyComplex


def positive_negative(word_1,word_2, sing):
    if sing == "-":
        return MyComplex(complex(word_1), complex(word_2) * -1)
    else:
        return MyComplex(complex(word_1), complex(word_2))


def operation(equation):
    value_1 = positive_negative(equation[0], equation[2], equation[1])
    value_2 = positive_negative(equation[4], equation[6], equation[5])

    if equation[3] == "+":
        value_1 + value_2
    elif equation[3] == "-":
        value_1 - value_2
    elif equation[3] == "*":
        value_1 * value_2
    elif equation[3] == "/":
        value_1 / value_2


def absolute_value(value):
    MyComplex.abs(positive_negative(value[0], value[2], value[1]))


def engine():

        while 1:
            temp = input("write complex\n").split()
            if len(temp) == 3:
                absolute_value(temp)
            elif len(temp) == 7:
                operation(temp)
            else:
                print("wrong try one more time\n")
            temp_string = input("stop?[stop]\n")
            if temp_string == "stop":
                break


if __name__ == '__main__':
    engine()
