n=input('Inserire un intero("*" per terminare):')
somma=0
while n!='*':
    if int(n)<0:
        somma=somma+int(n)
    n=input('Inserire un intero("*" per terminare):')
print(somma)
