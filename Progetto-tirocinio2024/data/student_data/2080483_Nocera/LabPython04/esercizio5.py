n=int(input("inserisci un numero : ") )
if n>=0:
    if n==0:
        print(1)
    elif n==1:
        print(1)
    elif n>=2:
        k=0
        p=n
        c=1
        while k==0:
            p=p*c
            c=c+1
            if c==n:
                k=1
        print(p)
                
else: print("il numero inserito è negativo")
