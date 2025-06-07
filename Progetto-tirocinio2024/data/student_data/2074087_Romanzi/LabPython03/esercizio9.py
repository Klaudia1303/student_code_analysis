w=True
while w:
    n=int(input('Numero '))
    if n<=1:
        print('Numero non primo ')
    else:
        w=False
d=2
if n==2:
    print('Numero primo ')
while d<n:
    if n%d==0:
        print('Numero non primo ')
        d=n+1
    else:
        d=d+1
    if d==n:
        print('Numero primo ')
