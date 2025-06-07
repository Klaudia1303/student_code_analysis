i = False
k = 0
while not i:
    n = input('Inserire un numero intero, o * per terminare: ')
    if n == '*':
        i = True
    elif int(n) > 0:
        k += 1
print(k)
