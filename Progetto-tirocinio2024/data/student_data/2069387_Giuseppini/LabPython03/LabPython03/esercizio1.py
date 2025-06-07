n=int(input('inserisci un numero intero maggiore di due: '))
c=2
while c<=n:
    if n%2==0:
        print(c)
        c=c+2
    else:
        n=n-1
