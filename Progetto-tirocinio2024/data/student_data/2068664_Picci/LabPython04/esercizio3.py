n=input('inserisci intero:')
somma=0

while n!='*':
    if int(n)<0:
        somma=somma+int(n)
    n=input('inserisci intero:')

print('somma interi negativi=',somma)
