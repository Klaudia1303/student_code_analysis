zero = False
i = 0
while not zero:
    n = int(input("Inserire un numero intero: "))
    if n == 0:
        zero = True
    elif n%3 == 0:
        i += n
print(i)
