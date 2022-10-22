#Paweł Majewski EiT Programowanie w języku Python
#zad_18
# Napisz program proszący użytkownika o dane zawierające kilka
# pól (może to być np. lista zadań z opisem i terminami wykonania czy baza recenzji filmów) i zapisujący
# podane dane do pliku
# w wybranym formacie (CSV/JSON). Przy każdym uruchomieniu program powinien odczytywać i wyświetlać wprowadzone
# wcześniej dane, umożliwiać ich usunięcie (po jednym wpisie)
# oraz dodanie nowych rekordów.
import csv


def print_file():
    with open('data.csv', "r") as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for row in csv_read:
            print(row)


def add_row():
    while 1:
        try:
            name, surname, date = input("write name, surname, date\n").split()
            break
        except ValueError:
            print("try again\n")

    with open('data.csv', 'a', newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([name, surname, date])


def remove_row():
    with open('data.csv', 'r') as read, open('first_edit.csv', 'w',  newline='\n') as out:
        writer = csv.writer(out)
        for row in csv.reader(read):
            writer.writerow(row)

    while 1:
        try:
            name, surname, date = input("write name, surname, date to delete\n").split()
            break
        except ValueError:
            print("try again\n")

    with open('first_edit.csv', 'r') as read, open('data.csv', 'w',  newline='\n') as out:
        writer = csv.writer(out)
        for row in csv.reader(read):
            if row != [name, surname, date]:
                writer.writerow(row)


def engine():
    while 1:
        status = input("stop?[stop]\n")
        if status == "stop":
            break
        print_file()
        status = input("add or remove?\n")
        if status == "add":
            add_row()
        elif status == "remove":
            remove_row()
        else:
            print("bad status\n")


if __name__ == '__main__':
    engine()


