n = int(input('Inserisci un numero intero positivo: '))
k = 1
c = 0
while k <= n:
    if n%k == 0:
        c+=1
    k+=1
if c==2:
    print('Numero primo')
else:
    print('Numero non primo')
