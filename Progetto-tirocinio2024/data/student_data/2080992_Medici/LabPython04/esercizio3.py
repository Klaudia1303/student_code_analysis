somma=0
n=0
while n!='*':
    n=str(input('inserisci un numero intero: '))
    if n=='*':
        print(somma)
        break
    else:
        n=int(n)
        if n<0:
            somma+=n
