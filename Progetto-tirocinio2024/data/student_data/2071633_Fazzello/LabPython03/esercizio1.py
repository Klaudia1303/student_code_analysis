#1) Scrivere un programma python che chiede in input all’utente un intero n>2 e stampa tutti i numeri pari
#compresi tra 2 e n uno per riga (includendo 2 ed n). Esempio:
#• Inserendo l’intero “4”, il programma stampa “2” e a capo “4”
#• Inserendo l’intero “7”, il programma stampa “2”, a capo “4” e infine a capo “6”

n=input ("inserisci numero intero maggiore di 2 ")
n=int(n)
m=0
#if n%2==0:
while (m<n):
        m+=2
        if m<n:
            print(m)
        
