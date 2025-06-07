#2) Scrivere un programma python che chiede in input all’utente un numero intero maggiore di zero e
#stampa a schermo tutti i suoi divisori interi positivi. Esempio:
#•
#Inserendo l’intero “6”, il programma stampa “1”, a capo “2”, a capo “3”, a capo “6”

n=input("Inserisci numero maggiore di 0 ")
n=int(n)
m=1

while m<=n:
    if n%m==0:
        print(m)
    m+=1
