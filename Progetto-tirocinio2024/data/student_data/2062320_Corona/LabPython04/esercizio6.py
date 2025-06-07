n1=int(input())
n2=int(input())
prodotto=0
i=0
if n2<0:
    i=-n2
else:
    i=n2
while i>0:
    prodotto+=n1
    i-=1
if n2>0:
    print(prodotto)
else:
    print(-prodotto)