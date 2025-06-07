i=1
prodotto=0
n1=int(input('inserire un numero intero: '))
n2=int(input('inserire un numero intero: '))
if n1<0 and n2<0:
    n2=abs(n2)
    n1=abs(n1)
    while i<n2+1:
        prodotto+=n1
        i+=1
    print(prodotto)
elif n2<0 or n1<0:
    n2=abs(n2)
    n1=abs(n1)
    while i<n2+1:
        prodotto+=n1
        i+=1
    print(-prodotto)
else:
    while i<n2+1:
        prodotto+=n1
        i+=1
    print(prodotto)
    

    
