finito = False
while not finito:
    n = int(input("Numero: "))
    if n % 5 == 0:
        finito = True
print(n // 5)
