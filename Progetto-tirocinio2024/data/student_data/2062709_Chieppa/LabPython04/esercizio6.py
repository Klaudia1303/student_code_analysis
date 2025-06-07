n=int(input('inserire numero intero: '))
m=int(input('inserire numero intero: '))
x=1
prodotto=0
while x<=abs(m):
    prodotto=prodotto+n
    x=x+1
if n<0 and m<0 or m<0:
    prodotto=-prodotto
print(prodotto)

