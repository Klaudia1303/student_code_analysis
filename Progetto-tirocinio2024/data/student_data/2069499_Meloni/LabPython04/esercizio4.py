n=input('Inserisci un intero (0 per terminare) ')
somma=0
while (n!='0'):
    if(int(n)%3==0):
        somma+=int(n)
    n=input('Inserisci un intero (0 per terminare) ')
print (somma)
