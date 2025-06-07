n1=int(input('inserisci un numero intero: '))
n2=int(input('inserisci un numero intero: '))
prodotto=0
if n2>0:
    i=1
    while i<=n2:
        prodotto=prodotto+n1
        i=i+1
    print('il prodotto vale:',prodotto)
if n2<0:
    i=-1
    while i>=n2:
        prodotto=prodotto-n1
        i=i-1
    print('il prodotto vale:',prodotto)
