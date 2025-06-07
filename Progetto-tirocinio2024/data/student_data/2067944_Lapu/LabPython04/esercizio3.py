ast = False
i = 0
while not ast:
    n = input("Inserire un numero intero: ")
    if n == '*':
        ast = True
    elif int(n) < 0:
        i += int(n)
print(i)
