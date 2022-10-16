#Paweł Majewski EiT Programowanie w języku Python
#zad_13
import random
n = 4
if __name__ == '__main__':

    c = [[0]*n for i in range(n)]
    d = [[0]*n for i in range(n)]
    e = [[0]*n for i in range(n)]

    #rozmiar nowej macierzy
    for i in range(0,n):
        for j in range(0,n):
            c[i][j] = random.randint(0,200)
            d[i][j] = random.randint(0,200)

    for i in range(0,n):
        print(c[i])
    print("\n")
    for i in range(0,n):
        print(d[i])
    print("\n")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                e[i][j] = e[i][j] + c[i][k] * d[k][j]

    for i in range(0,n):
        print(e[i])
