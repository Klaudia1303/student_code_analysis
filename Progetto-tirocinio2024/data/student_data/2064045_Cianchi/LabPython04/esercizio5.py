n=int(input('inserire un intero maggiore o uguale a 0:'))
if n<0:
    n=int(input('errore, inserire un intero maggiore o uguale a 0:'))
if n==0 or n==1:
    print('il fattoriale vale:',1)
fattoriale=1
i=1
while n>=i:
    fattoriale=fattoriale*i
    i+=1
print('il fattoriale vale:',fattoriale)
