c=int(input("Inserire un numero maggiore di 1:  "))
if c<=1:
    print("errore")
else:
    n=2
    while n<=c:
        d=0
        x=1
        while x<=n:
            if n%x==0:
                d=d+1
            x=x+1
        if d==2:
            print(n)
        n += 1
                
