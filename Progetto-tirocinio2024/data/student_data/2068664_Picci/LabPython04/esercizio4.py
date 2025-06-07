n=int(input('inserisci numero intero:'))
somma=0

while n!=0:
    if n%3==0:
        somma=somma+n
    n=int(input('inserisci numero intero:'))

print(somma)
