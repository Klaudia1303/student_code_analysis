ast = False
k = 0
while not ast:
    n = input('Inserisci un numero intero: ')
    if n == '*':
        ast = True
    elif int(n) < 0:
        k += int(n)
print(k)
