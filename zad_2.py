#Paweł Majewski EiT Programowanie w języku Python
#zad_2

def print_data(name, surname, date):
    print("Your name= "+name+"\n")
    print("Your surname= "+surname+"\n")
    print("Your date= "+date+"\n")

if __name__ == '__main__':
    while 1:
        try:
            name, surname, date = input("podaj imie, nazwisko, rok urodzenia\n").split()
            break;
        except ValueError:
            print("zle dane, jeszcze raz\n")
    print_data(name,surname,date)