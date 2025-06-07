n=int(input('inserisci intero >=0: '))
prec=n-1
prod=n
if n==0 or n==1:
    print(1)
else:
    while prec!=1:
        prod=prod*prec
        prec=prec-1
    print(prod)
    
