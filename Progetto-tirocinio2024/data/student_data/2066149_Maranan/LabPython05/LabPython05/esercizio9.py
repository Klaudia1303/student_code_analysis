n = int(input('Inserisci un intero dispari maggiore o uguale a 3: '))
for i in range(n):
    if i == 0 or i == n-1:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
