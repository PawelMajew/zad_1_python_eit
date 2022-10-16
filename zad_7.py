#Paweł Majewski EiT Programowanie w języku Python
#zad_7

if __name__ == '__main__':
    text_file = open("text_1.txt", "r+")

    temp = text_file.read()
    #trzeba dodać spacje na końcu słowa
    vowel = ["i","jak","pojęcia"]
    for i in vowel:
        temp = temp.replace(i, "")

    print(temp)