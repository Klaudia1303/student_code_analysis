n=int(input('inserisci un intero maggiore di 1: '))
c=2
while c<=n:
    a=2
    while a<c:
        if c%a==0:
            a=c
        a=a+1
    if a==c:
        print (c)
    c=c+1
