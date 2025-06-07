n = int(input('Inserisci un intero dispari maggiore o uguale a 3: '))
for i in range(1, n+1, 2):
    print (' '*int(((n-1)/2)) + '*'*i)
    n -= 2
    
