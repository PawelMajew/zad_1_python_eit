#Paweł Majewski EiT Programowanie w języku Python
#zad_14
import random
n = 5
if __name__ == '__main__':
    a = [[0] * n for i in range(n)]

    # rozmiar nowej macierzy
    for i in range(0, n):
        for j in range(0, n):
            a[i][j] = random.randint(0, 200)

    for i in range(0, n):
        print(a[i])
    print("\n")
