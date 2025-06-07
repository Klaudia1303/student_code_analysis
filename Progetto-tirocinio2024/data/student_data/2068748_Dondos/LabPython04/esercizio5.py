n=int(input('Inserisci un intero >=0: '))
fattoriale=1

if n==0:
    print(fattoriale)
else:
    while n>1:
        fattoriale=n*fattoriale
        n=n-1
    print(fattoriale)
