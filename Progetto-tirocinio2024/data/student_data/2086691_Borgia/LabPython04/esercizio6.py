n1=int(input("Inseire il 1° numero: "))
n2=int(input("Inseire il 2° numero: "))
prodotto=n1
while n2!=1 and n2!=-1:
    if n2<0:
        n2+=1
    elif n2>0:
        n2-=1
    prodotto=prodotto+n1
if n2<0:
    print(0-prodotto)
else:
    print(prodotto)
