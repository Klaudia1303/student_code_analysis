n = int(input("Inserisci un intero:"))

if n%2 == 1:
    print(n)
    n = n-1
while n >= 2:
    print(n)
    n = n-2
