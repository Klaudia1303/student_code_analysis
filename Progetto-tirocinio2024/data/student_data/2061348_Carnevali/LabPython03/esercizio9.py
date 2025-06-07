n=int(input("inserire numero: "))
x=1
while x<=n:
    x=x+1
    if n%x==0 and x!=n:
        print("numero non primo")
        x=n+1
    elif x==n:
        print("numero primo")
        x=n+1
