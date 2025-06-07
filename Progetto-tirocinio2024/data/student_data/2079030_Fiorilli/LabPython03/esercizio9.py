n=int(input('inserisci un intero: '))
c=2
while c<n:
    if n%c==0:
        print('numero non primo')
        c=n
    c=c+1
if c==n:
    print('numero primo')
