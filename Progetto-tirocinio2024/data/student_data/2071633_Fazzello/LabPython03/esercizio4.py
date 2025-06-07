#4) Scrivere un programma python che chiede in input all’utente due numeri interi x e y compresi
#nell’intervallo [0,10] (assumete che i numeri immessi siano contenuti nell’intervallo) e stampa tutti i
#numeri fino a 10 esclusi x e y uno per riga. Esempio:
#•
#Inserendo gli interi “1” e “2”, il programma stampa “0” a capo “3” a capo “4” a capo “5” a capo
#“6” a capo “7” a capo “8” a capo “9” a capo “10”

x=input("Inserisci valore di x tra 0 e 10 ")
x=float(x)
y=input("Inserisci valore di y tra 0 e 10 ")
y=float(y)

var1=-1

while var1<10:
    var1+= 1
    if var1!=x and var1!=y:
            print (var1)

    
