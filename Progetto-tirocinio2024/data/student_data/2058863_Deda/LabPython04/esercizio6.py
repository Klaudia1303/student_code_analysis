n1=int(input('Inserisci intero numero 1 '))
n2=int(input('Inserisci intero numero 2 '))
prodotto=0
precedente=0
if n1>0 and n2>0:
    while n2>0:
        prodotto=n1+precedente
        precedente=prodotto
        n2=n2-1
    print(precedente)
elif n1<0 and n2<0:
    while n2<0:
        prodotto=n1+precedente
        precedente=prodotto
        n2=n2+1
    print(-precedente)
elif n1>0 and n2<0:
    while n1>0:
        prodotto=n2+precedente
        precedente=prodotto
        n1=n1-1
    print(precedente)
elif n1<0 and n2>0:
    while n2>0:
        prodotto=n1+precedente
        precedente=prodotto
        n2=n2-1
    print(precedente)
