n=int(input('Inserisci un intero (0 per terminare): '))
somma_ndiv3=0

while n!=0:
    if n%3==0:
        somma_ndiv3+=n
    n=int(input('Inserisci un intero (0 per terminare): '))
print(somma_ndiv3)
