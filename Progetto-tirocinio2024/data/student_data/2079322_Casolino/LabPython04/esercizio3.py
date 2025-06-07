i='0'
somma=0
while i!='*':
    i=input('Inserisci un numero intero, "*" se vuoi terminare: ')
    if i!='*':
        n=int(i)
        if n<0:
            somma=somma+n
print(somma)
