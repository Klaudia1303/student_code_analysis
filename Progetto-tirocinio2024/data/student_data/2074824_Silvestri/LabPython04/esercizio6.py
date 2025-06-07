n1=int(input("Inserisci un intero:"))
n2=int(input("Inserisci un intero:"))
c=n2
prodotto=0
if n1<0 and n2<0:
    c=c*-1
    c2=-n1
    while c>0:
        prodotto+=c2
        c-=1
elif n1>0 and n2>0:
    while c>0:
        prodotto+=n1
        c-=1
elif (n1<0 and n2>0) or (n1>0 and n2<0):
    negativo=min(n1,n2)
    positivo=max(n1,n2)
    c3=negativo*-1
    while c3>0:
        prodotto+=positivo
        c3-=1
        prodotto=prodotto*-1
else:
    prodotto=0
print("Il prodotto dei due numeri è:", prodotto)
     
