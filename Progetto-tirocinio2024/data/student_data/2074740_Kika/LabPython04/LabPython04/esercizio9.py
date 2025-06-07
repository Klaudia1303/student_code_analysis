n=int(input('inserisci intero >0: '))
prec=0
succ=1
somma=prec+succ
k=1
print(1)
while k!=n:
    print(somma)
    prec=succ
    succ=somma
    somma=prec+succ
    k=k+1
