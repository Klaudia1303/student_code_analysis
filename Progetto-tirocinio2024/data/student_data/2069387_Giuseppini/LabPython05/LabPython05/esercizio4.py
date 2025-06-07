#Scrivere programma che chiede in input all’utente 2 numeri interi positivi n1 e n2 e stampa (1 per riga)
#in ordine crescente i multipli di n1 (incluso n1) che sono strettamente più piccoli di n2.

n1=int(input('inserisci un numero: '))
n2=int(input('non superiore di n: '))

for i in range(1,n2):
    m=i*n1
    if m<n2:
        print(m)
