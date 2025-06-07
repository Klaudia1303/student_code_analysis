n=int(input('inserisci un intero uguale o maggiore di 0:'))
tot=1
if n==0 or n==1:
    print('Il prodotto fattoriale è:',1)

while n>1:
    tot*=n
    n-=1
print('Il prodotto fattoriale è:',tot)
