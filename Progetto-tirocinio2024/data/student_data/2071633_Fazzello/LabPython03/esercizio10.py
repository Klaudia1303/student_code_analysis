#10) Scrivere un programma python che chiede in input all’utente un numero intero positivo n maggiore di 1
#e stampa uno per riga tutti i numeri primi compresi tra 2 e n, includendo 2 ed n (qualora fosse primo).
#Esempio:
#• Inserendo il numero “9”, il programma stampa “2”, a capo “3”, a capo “5”, a capo “7

n=0
while n<=1:
    n=input("Inserisci un numero maggiore di 1:")
    n=int(n)
k=2
x=2
while k<=n:
    if k%x==0 and x!=k:
        x=1
        k=k+1
    elif x>k:
        print(k)
        x=1
        k=k+1
    x=x+1
