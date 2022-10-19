#Paweł Majewski EiT Programowanie w języku Python
#zad_3
# Napisz skrypt realizujący funkcję zamka szyfrowego. Prosi
# o podanie kodu i następnie sprawdza czy jest on zgodny z
# wcześniej wprowadzonym kodem
def get_code():
    return input("ustaw kod\n")


def check_code(code_true):
    while 1:
        input_code = input("podaj kod\n")
        if input_code == code_true:
            print("wlasciwy kod\n")
            break
        else:
            print("zly kod!!\n")


if __name__ == '__main__':

    code_true = get_code()
    check_code(code_true)