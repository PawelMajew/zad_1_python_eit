#Paweł Majewski EiT Programowanie w języku Python
#zad_2
# Napisz skrypt, który pyta o imię, nazwisko i rok urodzenia
# (powinny być podane w jednej linii)

def print_data(name, surname, date):
    print("Your name= "+name+"\n")
    print("Your surname= "+surname+"\n")
    print("Your date= "+date+"\n")


def get_and_print():
    while 1:
        try:
            name, surname, date = input("podaj imie, nazwisko, rok urodzenia\n").split()
            break
        except ValueError:
            print("zle dane, jeszcze raz\n")
    print_data(name,surname,date)


if __name__ == '__main__':
    get_and_print()