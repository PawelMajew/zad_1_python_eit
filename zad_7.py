#Paweł Majewski EiT Programowanie w języku Python
#zad_7

if __name__ == '__main__':
    text_file = open("text_1.txt", "r+")

    temp_text = text_file.read()

    list = ["a ","ku ","widzi "]
    for next_element in list:
        temp_text = temp_text.replace(next_element, "")

    print(temp_text)