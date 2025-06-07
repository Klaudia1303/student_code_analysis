n=int(input('Inserisci una numero: '))
i=2
if n==2:
    print('Il numero è primo')
else:
    while n%i!=0 and i<(n-1):
        i+=1
    if n%i==0:
        print('Il numero non è primo')
    elif n%i!=0:
        print('Il numero è primo')