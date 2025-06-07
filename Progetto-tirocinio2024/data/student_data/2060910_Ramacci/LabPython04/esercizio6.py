n=int(input("inserire un numero intero: "))
m=int(input("inserire un numero intero: "))
if m==0 and n==0:
    prodotto=0
elif n>0 and m>0:
    prodotto=0
    r=0
    while m>r:
        prodotto+=n
        m-=1
elif (n>0 and m<0) or (n<0 and m>0):
    prodotto=0
    r=0
    t=max(n,m)
    while t>r:
        prodotto+=min(n,m)
        t-=1
else:
    prodotto=0
    r=0
    while m<r:
        prodotto-=n
        m+=1
print(prodotto)
