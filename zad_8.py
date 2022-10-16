#Paweł Majewski EiT Programowanie w języku Python
#zad_8

if __name__ == '__main__':
    text_file = open("text_1.txt", "r+")

    temp = text_file.read()
    #trzeba dodać spacje na końcu słowa
    vowel = ["i ","jak ","pojęcia "]
    for i in vowel:
        if i == vowel[0]:
            temp = temp.replace(i, "elo ")
        elif i == vowel[1]:
            temp = temp.replace(i, "lol ")

    print(temp)