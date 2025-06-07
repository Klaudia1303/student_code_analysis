prodotto=0
n1=int(input('Inserisci un intero: '))
n2=int(input('Inserisci un intero: '))
if n1==0 or n2==0:
    print(prodotto)
while n2!=0:
    if n2<0:
        if n1>0 or n1<0:
            prodotto=prodotto-n1
            n2+=1
    elif n2>0:
        prodotto=prodotto+n1
        n2-=1
    if n2==0:
        print(prodotto)
