n=int(input('inserire un numero intero:'))
somma=0
while n!='*':
    n=input('inserire un numero intero (* per terminare):')
    if n!='*' and int(n)<0:
        somma=somma+int(n)
print('totale =',somma)
