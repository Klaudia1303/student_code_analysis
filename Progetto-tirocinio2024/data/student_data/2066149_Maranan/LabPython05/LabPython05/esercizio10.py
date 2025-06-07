n = int(input('Inserisci un intero dispari maggioreo uguale a 2: '))
if n <= 4:
    print(('*'*n+'\n')*n)
else:
    for i in range(n):
        for j in range(n):
            if i == j or n-j-1 == i or j == 0 or j == n-1 or i == 0 or i == n-1:
                print('*', end='')
            else:
                print(' ',end='')
        print('')
            
                
