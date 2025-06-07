n1 = int(input("Inserire un numero intero maggiore di 0:"))
n2 = int(input("Inserire un numero intero maggiore di 0:"))

if n1 > n2:
    i = n1
else:
    i = n2

while i > 0:
    if n1 % i == 0:
        if n2 % i != 0:
            print(i)
    i -= 1
