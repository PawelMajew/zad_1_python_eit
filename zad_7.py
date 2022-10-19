#Paweł Majewski EiT Programowanie w języku Python
#zad_7
# Napisz skrypt usuwający z wejściowego ciągu tekstowego
# (wybierz kilka plików z repozytorium: Tekstowego) następujące
# słowa : się, i, oraz, nigdy, dlaczego


def delete_word(file):
    temp_text = file.read()
    print(temp_text + '\n')

    list = ["a ", "ku ", "widzi "]
    for next_element in list:
        temp_text = temp_text.replace(next_element, "")

    print(temp_text + '\n')


if __name__ == '__main__':

    text_file = open("text_1.txt", "r")
    delete_word(text_file)
