#Paweł Majewski EiT Programowanie w języku Python
#zad_8

if __name__ == '__main__':
    text_file = open("text_1.txt", "r+")

    temp_text = text_file.read()

    list = ["a ","ku ","widzi "]
    for next_element in list:
        if next_element == list[0]:
            temp_text = temp_text.replace(next_element, "ale ")
        elif next_element == list[1]:
            temp_text = temp_text.replace(next_element, "tak ")
        elif next_element == list[2]:
            temp_text = temp_text.replace(next_element, "patrzy ")

    print(temp_text)