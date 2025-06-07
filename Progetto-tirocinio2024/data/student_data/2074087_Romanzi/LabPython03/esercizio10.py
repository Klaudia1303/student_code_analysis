w=True
while w:
    n=int(input('Numero '))
    if n<=1:
        print('Numero minore o uguale a 1 ')
    else:
        w=False
p=2
d=2
while p<=n:
    while d<=p:
        if p%d==0 and p!=d:
            d=p+1
        elif d==p:
            print(p)
            d=p+1
        else:    
            d=d+1
    d=2
    p=p+1
