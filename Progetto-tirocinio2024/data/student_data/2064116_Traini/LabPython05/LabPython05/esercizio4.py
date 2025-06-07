#Scrivere programma che chiede in input all’utente 2 numeri interi positivi n1 e n2 e stampa (1 per riga) 
#in ordine crescente i multipli di n1 (incluso n1) che sono strettamente più piccoli di n2. Esempi:
#• inserendo gli interi 5 e 16, il programma stampa 5, a capo 10, a capo 15
#• inserendo gli interi 3 e 15, il programma stampa 3, a capo 6, a capo 9, a capo 12
#• inserendo gli interi 7 e 8, il programma stampa 7
i=int(input('inserisci un intero positivo: '))
j=int(input('inserisci un intero positivo: '))
for a in range(j):
    if a%i==0:
        print(a)
    
