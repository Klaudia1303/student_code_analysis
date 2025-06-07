somma = 0
while True:
    n = int(input("Numero: "))
    if n == 0:
        break
    elif n % 3 == 0:
        somma += n
print(somma)
