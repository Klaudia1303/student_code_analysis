zero = False
k = 0
while not zero:
    n = int(input('Inserisci un numero intero: '))
    if n == 0:
        zero = True
    elif n%3 == 0:
        k += int(n)
print(k)
