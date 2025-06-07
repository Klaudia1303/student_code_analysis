n=int(input("Inserisci un numero intero"))
i=2
n1=1
n2=1
cond = False
se = False
if n==1:
    print(1)
    cond = True
elif n==2:
    print(1)
    print(1)
    cond = True
while not cond:
    while i<n:
        if not se:
            print(1)
            print(1)
            se = True
        somma=n1+n2
        print(somma)
        n1=n2
        n2=somma
        i+=1
    
        
