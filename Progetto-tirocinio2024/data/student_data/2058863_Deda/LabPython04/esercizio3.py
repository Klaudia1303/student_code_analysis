s='3'
n=int(s)
somma=0
precedente=0
x='*'
while s!=x:
    if s!=x:
        s=input('Inserisci intero o "*" per terminare ')
        if s!=x:
            n=int(s)
            if n<0:
                somma=precedente+n
                precedente=somma
            elif n>0:
                somma=precedente
print(somma)
