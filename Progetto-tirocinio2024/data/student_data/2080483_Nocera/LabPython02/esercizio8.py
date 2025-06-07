#Scrivere un programma che prende in ingresso 3 interi a, b, c, e determina se essi possano rappresentare le
#lunghezze dei lati di un triangolo
a = int(input("scrivere un intero :"))
b = int(input("scrivere un intero :"))
c = int(input("scrivere un intero :"))
if a>0 and b>0 and c>0 and a<b+c and b<a+c and c<a+b :
    print("è un triangolo")
    if a!=b and b!=c and a!=c:
        print("scaleno")
    elif (a==b and a!=c) or (b==a and b!=c) or (c==a and c!=b):
        print("isoscele")
    elif (a==b and a==c):
        print ("equilatero")
else:
    print("non è un triangolo")

        
