#Paweł Majewski EiT Programowanie w języku Python
#zad_6
from PIL import Image

if __name__ == '__main__':

    im1 = Image.open(r"E:\studia\semestr_VII\python\cw_labo\zad\lion.jpg")
    im1.save(r"E:\studia\semestr_VII\python\cw_labo\zad\lion.png")