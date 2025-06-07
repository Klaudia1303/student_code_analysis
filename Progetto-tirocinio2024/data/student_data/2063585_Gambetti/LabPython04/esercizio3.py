s=input('inserisci un numero intero (* per terminare): ')
somma=0
while s!='*':
    c=int(s)
    if c<=0:
        s=input('inserisci un numero intero (* per terminare): ')
        somma=somma+c
    elif c>0:
        s=input('inserisci un numero intero (* per terminare): ')
print(somma)
    

    
