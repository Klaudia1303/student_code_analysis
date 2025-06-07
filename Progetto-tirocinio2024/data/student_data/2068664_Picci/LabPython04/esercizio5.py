n=int(input('inserisci intero maggiore o uguale a 0:'))
fattoriale=1

while n>=0:
    if n>=1:
        fattoriale=fattoriale*n
    n=n-1

print('il fattoriale è:',fattoriale)
        
