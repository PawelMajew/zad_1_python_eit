#Paweł Majewski EiT Programowanie w języku Python
#zad_5
# Napisz rekurencyjne przejście drzewa katalogów i wypisanie
# plików, które znajdują się w eksplorowanej strukturze
import os


def show(path):

    for item in os.listdir(path):

        new_path = os.path.join(path, item);
        print("\n")
        print(new_path)
        print(("*")*70+"\n")
        print(item)
        if os.path.isdir(new_path):
            show(new_path)


if __name__ == '__main__':

    path = "E:\studia\semestr_VII\python\cw_labo\zad"
    show(path)