n=input('inserisci un numero intero (* per terminare) ')
somma=0
while n!='*':
    if n<'0':
        n=int(n)
        somma=somma+n
    n=input('inserisci un numero intero (* per terminare) ')
print(somma)
