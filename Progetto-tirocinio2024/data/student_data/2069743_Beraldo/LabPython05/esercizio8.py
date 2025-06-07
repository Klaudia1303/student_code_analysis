n=int(input('inserisci un numero dispari maggiore o uguale a 3'))
i=1
while i<=n:
    print((((n-i)//2)*' ')+i*'*'+(((n-i)//2)*' '))
    i+=2
