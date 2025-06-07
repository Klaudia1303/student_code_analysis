n=int(input("inserire numero: "))
x=0
while x<=n:
    y=1
    while y<=x:
        y=y+1
        if x%y==0 and y!=x:
            y=n+1
        elif y==x:
            print(x)
            y=n+1
    x=x+1
