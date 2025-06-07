n=int(input('Inserisci un intero n>2: '))
while n>=2:
    if n%2==0:
        print(n)
        n=n-2
    else:
        ndispari=n-1
        print(n-1)
        n=n-2