n=int(input("Inserire un numero diverso da 0:  "))
n=abs(n)
if n==0:
    print("errore")
else:
    d=0
    x=1
    while x<=n:
        if n%x==0:
            d=d+1
        x=x+1
    if d>2:
        print("Numero non primo")
    else:
        print(n,"è un  numero primo")
