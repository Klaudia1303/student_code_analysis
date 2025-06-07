n=int(input('inserisci un numero maggiore di 3 dispari:'))
for i in range(n+1):
    if i % 2 == 1:
        print(' '*((n-i)//2) + '*'*i )
