n = int(input("Inserisci un intero dispari e maggiore o uguale a 3: "))
for i in range(n+1):
    if i % 2 == 1: 
        print(' '*((n-i)//2) + '*'*i + ' '*((n-i)//2))
