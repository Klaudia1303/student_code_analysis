n=int(input('inserire un intero:'))
somma=0
while n!='0':
    n=input('inserire un intero (0 per terminare):')
    if int(n)!='0' and int(n)%3==0:
        somma=somma+int(n)
print('totale =',somma)
