n=int(input('Inserire un intero maggiore o uguale a 0:'))
while n<0:
    n=int(input('Inserire un intero maggiore o uguale a 0:'))
somma=1
contatore=2
while contatore<=n:
    somma=somma*contatore
    contatore+=1
print(somma)

