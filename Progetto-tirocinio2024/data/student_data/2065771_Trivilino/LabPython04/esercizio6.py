n=int(input('Inserire un numero intero: '))
z=int(input('Inserire un secomdo numero intero: '))
prodotto=0
c=z
while abs(c)>0:
    prodotto+=n
    c=abs(c)-1
if z<0:
    print(-prodotto)
else:
    print(prodotto)
