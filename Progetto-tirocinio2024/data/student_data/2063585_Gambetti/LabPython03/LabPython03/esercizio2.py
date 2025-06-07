n=int(input('inserisci un numero intero: '))
i=1
while 1<=i<=n:
    divisori=n%i
    if divisori==0:
        print(i)
    i=i+1
