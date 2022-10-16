#Paweł Majewski EiT Programowanie w języku Python
#zad_11

if __name__ == '__main__':
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    c = 0
    for i in range(0,len(a)):
        c += a[i]*b[i]

    print(c)