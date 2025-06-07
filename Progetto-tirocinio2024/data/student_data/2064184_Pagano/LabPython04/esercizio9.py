n = int(input("Inserisci un intero maggiore di 0: "))

print(1)

fiboPrev = 0
fiboLast = 1

for i in range(1, n):
    fibo = fiboPrev + fiboLast
    fiboPrev = fiboLast
    fiboLast = fibo
    print(fibo)
