n=int(input("inserire un numero "))
s=int(input("inserire un numero "))
m=0
prodotto=0
if s<0:
    s=-s
    n=-n
a=n
while m<s:
    m+=1
    prodotto=prodotto+a
print(prodotto)
