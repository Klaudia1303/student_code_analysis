n = int(input('Inserisci un numero intero maggiore o uguale a 0: '))
f = 1
while n!=0:
    f *= n
    n -= 1
print(f)
