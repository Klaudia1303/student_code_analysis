#Scrivere un programma python che chiede in input all’utente un intero n maggiore di 0 e stampa uno per
#riga i primi n numeri della successione di Fibonacci. I primi due numeri della successione di Fibonacci
#sono 1 ed 1, ed ogni numero successivo è dato dalla somma dei due precedenti. Quindi avremo: 1 1 2 3 5
#8 13 21 34...
#Esempio:
#Inserendo l’intero “6”, il programma stampa “1”, a capo “1”, a capo “2”, a capo “3”, a capo “5”, a capo
#“8”.
n= int(input("inserisci un numero intero maggiore di 0 : "))
n1=1
n2=1
i=0
f=0
while i<n-1:
    f=n2
    n2=n1+n2
    n1=f
    i+=1
    print(n1)


    
