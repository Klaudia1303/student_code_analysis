n=int(input('inserisci un intero maggiore di zero: '))
while n<=0:
    n=int(input('inserisci un intero maggiore di zero: '))
succ=1
prec=0
c=1
print (succ)
while c<n:
    print (prec+succ)
    d=succ
    succ=succ+prec
    prec=d
    c+=1    
