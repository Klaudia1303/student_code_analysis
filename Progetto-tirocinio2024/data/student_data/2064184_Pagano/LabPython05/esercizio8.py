b = int(input("Inserisci un intero dispari >= 3: "))

for i in range(1, b+1, 2):
    print(' '*((b-(i-1))//2), '*'*i, sep='')
