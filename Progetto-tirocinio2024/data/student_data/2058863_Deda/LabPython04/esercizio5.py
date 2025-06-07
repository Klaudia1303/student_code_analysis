n=int(input('Inserisci intero '))
precedente=1
while n>1:
    if n>1:
        prodotto=precedente*n
        precedente=prodotto
        n=n-1
print(precedente)
