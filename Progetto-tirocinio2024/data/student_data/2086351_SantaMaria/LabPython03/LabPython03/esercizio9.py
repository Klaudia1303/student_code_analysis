n=int(input('Inserisci un intero: '))
i=2
while i<n:
    if n%i!=0:
        i+=1
    else:
        print('numero non primo')
        i=n+1
if i==n:
    print('numero primo')
