somma=0
n=3
while n!='*':
    n=input('Inserisci un intero(* per terminare): ')
    if n=='*':
        print(somma)
    elif int(n)<0:
        n=int(n)
        somma=somma+n
