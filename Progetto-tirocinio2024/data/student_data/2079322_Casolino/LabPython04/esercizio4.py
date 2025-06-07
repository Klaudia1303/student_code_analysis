i='*'
somma=0
while i!='0':
    i=input('Inserisci un numero intero, "0" se vuoi terminare: ')
    if i!='0':
        n=int(i)
        if n%3==0:
            somma=somma+n
print(somma)
