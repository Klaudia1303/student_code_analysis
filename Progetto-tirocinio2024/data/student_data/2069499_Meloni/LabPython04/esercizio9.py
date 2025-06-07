n=int(input('Inserisci un intero maggiore di 0 '))
i=0
primo=1
secondo=1
somma=1
print('1')
while (i<n-1):
    print(somma)
    somma=primo+secondo
    secondo=primo
    primo=somma
    
    i+=1
