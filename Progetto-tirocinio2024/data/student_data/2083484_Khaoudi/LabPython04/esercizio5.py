#5) Scrivere un programma python che chiede in input all’utente un intero maggiore o uguale a 0 e stampa il
#suo fattoriale. Si ricorda che il fattoriale un numero intero n, indicato con n!, è pari a 1 se n=0 e se n=1,
#ed è invece pari al prodotto dei numeri interi positivi minori o uguali a n se n>1.
#Esempio:
#•
#Inserendo l’intero “5”, il programma stampa “120” ottenuto in quanto 5! = 5*4*3*2*1
n = int(input("inserisci un numero :"))

i=1
f=1
while i<=n:
        f=f*i
        i=i+1

print(f)
