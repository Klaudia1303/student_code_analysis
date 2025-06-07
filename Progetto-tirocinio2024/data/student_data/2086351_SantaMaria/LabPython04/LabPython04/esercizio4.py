somma=0
n=3
while n!=0:
    n=int(input('Inserisci un intero(0 per terminare): '))
    if n==0:
        print(somma)
    elif n%3==0:
        somma=somma+n
