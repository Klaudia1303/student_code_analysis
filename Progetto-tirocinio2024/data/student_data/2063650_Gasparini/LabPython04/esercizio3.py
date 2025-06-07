somma = 0
while True:
    n = input("Numero: ")
    if n == "*":
        break
    elif int(n) < 0:
        somma += int(n)
print(somma)
