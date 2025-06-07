n1=int(input('Inserisci un intero: '))
n2=int(input('Inserisci un intero: '))
count=0
prodotto=0

if n1<=n2 or n1<0:
    while count<n2:
        prodotto+=n1
        count+=1
    print(prodotto)

elif n2<n1 or n2<0:
    while count<n1:
        prodotto+=n2
        count+=1
    print(prodotto)
