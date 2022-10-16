#Paweł Majewski EiT Programowanie w języku Python
#zad_9
#dodac możliwość wpisywania kilka razy i wykluczenie źle wpisanych liczb
import math
if __name__ == '__main__':
    print("init")
    a, b, c = input("podaj wartosci rownania a, b, c\n").split()
    print(a,b,c)
    a=int(a)
    b=int(b)
    c=int(c)
    if(a==0):
        print("to nie jest rownanie kwadratowe\n")
    if(a!=0):
        delta = b*b-4*a*c
        if(delta>0):
            x1 =(-b-math.sqrt(delta))/(2*a)
            x2 =(-b+math.sqrt(delta))/(2*a)
            print(x1,x2)
        if(delta<0):
            print("brak rozwiazania\n")
        if(delta==0):
            x1= -b/(2*a)
            print(x1)