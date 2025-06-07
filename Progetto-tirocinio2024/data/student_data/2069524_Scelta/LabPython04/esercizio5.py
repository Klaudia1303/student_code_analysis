n=int(input('Inserisci n intero maggiore uguale a 0: '))
fattoriale=1
if n==0 or n==1:
    fattoriale==1
    n-=1
while n>1:
        fattoriale*=n
        n-=1
print(fattoriale)

