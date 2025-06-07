n=int(input('Inserisci intero maggiore di 0 '))
while n<=0:
    if n<=0:
        print('Hai inserito un intero minore o uguale a 0')
        n=int(input('Inserisci intero maggiore di 0 '))
i=0
precedente1=0
precedente2=1
successivo=1
print('1')
while (i+1)<n:
    successivo=precedente1+precedente2
    precedente1=precedente2
    precedente2=successivo
    i+=1
    print(successivo)
