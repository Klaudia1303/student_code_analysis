somma=0
boo=True

while boo:
    n=input('inserisci un numero intero (inserisci * per terminare): ')
    if n=='*':
        boo=False
    elif int(n)<0:
        somma+=int(n) 
        
        
print(somma)
