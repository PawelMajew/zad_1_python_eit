#Paweł Majewski EiT Programowanie w języku Python
#zad_4
# Napisz skrypt zliczający ilość plików w katalogu /dev, skorzystaj
# ze standardowej biblioteki - os

import os


def show_count(path):
    with open('FileData_count.txt', 'w') as  file_output:
        # with path.open('r') as f

        for path, subfiles, files in os.walk(path):
            file_output.write('=' * 70 + '\n')
            file_output.write(path + '\n')
            if len(files):
                count = 0
                for i in files:
                    count += 1
                file_output.write("ilosc plikow: " + str(count) + '\n')
            else:
                file_output.write("ilosc plikow: 0\n")
    # file_output.close()


if __name__ == '__main__':

    path = "E:\studia\semestr_VII\python\cw_labo\zad"
    show_count(path)