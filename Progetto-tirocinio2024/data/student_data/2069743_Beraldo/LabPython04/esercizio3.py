aste = False
i = 0
while not aste:
    n = input("Inserire un numero intero: ")
    if n == '*':
        aste = True
    elif int(n) < 0:
        i += int(n)
print(i)
