#trova il fattoriale di un intero

n = int(input("intero = "))
fattoriale = n

if 0 <= n < 2:
    print(1)
else:
    while n > 1:
        fattoriale = fattoriale*(n-1)
        n = n-1
    print(fattoriale)
