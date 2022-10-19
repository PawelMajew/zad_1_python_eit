#Paweł Majewski EiT Programowanie w języku Python
#zad_8
# Napisz skrypt zmieniający w podanym ciągu wejściowym
# (wybierz kilka plików z repozytorium: Tekstowego) następujące
# słowa : i, oraz, nigdy, dlaczego na następujący zestaw słów : oraz,
# i, prawie nigdy, czemu. Zalecaną strukturą jest słownik.

def replace_word(file):
    temp_text = file.read()
    slownik = {' a ': 'tak ', ' ku ': 'ale ', ' widzi ': 'patrzy '}
    print(temp_text+'\n')

    for next_element in slownik:
        temp_text = temp_text.replace(next_element, slownik[next_element])

    print(temp_text)


if __name__ == '__main__':
    text_file = open("text_1.txt", "r+")
    replace_word(text_file)
