s=input('inserisci un numero intero (0 per terminare): ')
somma=0
while s!='0':
    c=int(s)
    if c%3==0:
        s=input('inserisci un numero intero (0 per terminare): ')
        somma=somma+c
    elif c%3!=0:
        s=input('inserisci un numero intero (0 per terminare): ')
print(somma)
        
