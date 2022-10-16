#Paweł Majewski EiT Programowanie w języku Python
#zad_10
import random
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

tab = []
if __name__ == '__main__':
    for i in range(50):
        tab.append(random.randint(1,200))

    # print(tab)
    temp_1 = tab
    temp_2 = tab

    bubbleSort(temp_1)
    # print(temp_1)
    temp_2.sort()
    for i in range(50):
        if(temp_1[i] != temp_2[i]):
            print("not")
    # print("\n")
    #print(tab)