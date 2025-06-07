n=int(input('inserire numero intero: '))
x=2
while x<=n:
    y=1
    y=y+1
    while y<x and x%y!=0:
        y=y+1
    if x==y:
        print(x)
    x=x+1

