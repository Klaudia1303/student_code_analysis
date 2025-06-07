false='*'
i=0
somma=0
while i>=0:
    s=input('inserisci un numero')
    if s!='*':
        n=int(s)
        if n<=0:
            somma=somma+n
    else:
        i=-1

print(somma)
