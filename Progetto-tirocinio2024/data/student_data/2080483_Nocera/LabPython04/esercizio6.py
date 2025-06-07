n=int(input("inserisci un numero :"))
l=int(input("inserisci un numero :"))
i=0
c=1
p=n
if l==0:
    print(0)
else:
    while i==0:
        n=n+p
        c= c+1
        if c==l:
            i=1
        elif -c==l:
            i=1
            n=-n
    print(n)
    
    
