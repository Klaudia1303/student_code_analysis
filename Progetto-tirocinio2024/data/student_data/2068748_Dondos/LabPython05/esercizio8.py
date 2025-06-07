n = int(input('Inserisci base triangolo (intero dispari >= 3): '))
space = n//2
for i in range (1, n+1, 2):
    print(' '*space + '*'*i + ' '*space)
    space-=1
