n = int(input("Inserisci un numero intero maggiore o uguale a 0: "))
while n < 0:
    n = int(input("Input non valido. Inserisci un numero intero maggiore o uguale a 0:"))
f = n
while n > 1:
    n -= 1
    f *= n
if n == 0:
    print("Fattoriale di 0: 1")
else:
    print("Fattoriale di ", n, ": ", f)
