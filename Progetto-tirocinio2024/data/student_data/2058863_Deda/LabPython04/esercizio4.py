n=int(input('Inserisci intero '))
x=0
precedente=0
somma=0
while n!=0:
    if n%3==0:
        somma=precedente+n
        precedente=somma
    elif n%3!=0:
        somma=precedente
    n=int(input('Inserisci intero '))
print(somma)
