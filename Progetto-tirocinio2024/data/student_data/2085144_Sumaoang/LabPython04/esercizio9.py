n = int(input("Inserire un numero intero maggiore di 0:"))
i = 1
j = 1

if n > 0:
    print(i)
while i < n and j < n:
    i += j
    print(i)
    if i < n and j < n:
        j += i
        print(j)

