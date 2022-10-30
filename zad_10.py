#Paweł Majewski EiT Programowanie w języku Python
#zad_10
# Napisz skrypt sortujący liczby malejąco. Wygeneruj losowo 50
# liczb - wykorzystąj standardową funkcje do losowania. Z wbudowanej funkcji sortującej korzystaj tylko
# w celu weryfikacji wyników

import random


def My_Sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


def Check_Sort(my_tab, correct_sort):
    not_correct_count = 0
    for next_item in range(50):
        if correct_sort[next_item] != my_tab[next_item]:
            not_correct_count+=1
    if not_correct_count == 0:
        print("sorted correct\n")
    else:
        print("sorted not correct\n")


def main():
    tab = []
    temp_tab_1 = []
    for i in range(50):
        tab.append(random.randint(1,200))
    for i in range(50):
        temp_tab_1.append(tab[i])

    My_Sort(tab)                #my sort
    temp_tab_1.sort()           #correct sort
    Check_Sort(tab,temp_tab_1)  #test


if __name__ == '__main__':
    main()
