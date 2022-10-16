#Paweł Majewski EiT Programowanie w języku Python
#zad_3

def get_code():
    return input("ustaw kod\n")
def check_code(code_true):
    while 1:
        input_code = input("podaj kod\n")
        if(input_code == code_true):
            print("wlasciwy kod\n")
            break;
        else:
            print("zly kod!!\n")

if __name__ == '__main__':
    code_true = get_code()
    check_code(code_true)