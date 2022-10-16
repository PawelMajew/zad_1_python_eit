#Paweł Majewski EiT Programowanie w języku Python
#zad_12
import random

if __name__ == '__main__':
    n = 5
    c = [[0]*n for i in range(n)]
    d = [[0]*n for i in range(n)]
    e = [[0]*n for i in range(n)]
    # print(c)

    for i in range(0,n):
        for j in range(0,n):
            c[i][j] = random.randint(0,200)
            d[i][j] = random.randint(0,200)


    for i in range(0,n):
        print(c[i])

    print("+++++++++++++")
    for i in range(0,n):
        print(d[i])

    for i in range(0,n):
        for j in range(0,n):
            e[i][j] = c[i][j] +d[i][j]

    print("***************")
    for i in range(0,n):
        print(e[i])