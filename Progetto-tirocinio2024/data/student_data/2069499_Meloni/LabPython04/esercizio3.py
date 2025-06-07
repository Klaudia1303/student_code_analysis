n=input('Inserisci un intero (* per terminare) ')
somma=0
while (n!='*'):
    if(int(n)<0):
        somma+=int(n)
    n=input('Inserisci un intero (* per terminare) ')
print (somma)
