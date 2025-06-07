n=int(input('inserisci un intero: '))
k=int(input('inserisci un intero: '))
somma=0
if k>=0:
    for a in range(1,k+1):
        somma=somma+n
else:
    for a in range(k,0):
        somma=somma-n
print(somma)
    

    
    