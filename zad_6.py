#Paweł Majewski EiT Programowanie w języku Python
#zad_6
# Napisz skrypt konwersji rozszerzeń plików *.jpg na *.png (uprzednio stwórz zestaw 4 plików z rozszerzeniem *.jpg)
from PIL import Image


if __name__ == '__main__':

    image = Image.open(r"E:\studia\semestr_VII\python\cw_labo\zad\lion.jpg")
    image.save(r"E:\studia\semestr_VII\python\cw_labo\zad\lion.png")