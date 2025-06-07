n = int(input('Inserisci un numero intero: '))
m=2
while n%m!=0 and m<n:
    m += 1

if m==n:
    print('numero primo')
else:
    print('numero non primo')
