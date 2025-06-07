n = input("Inserisci il numero: ")
n_int = 0
while n != "*":
    n = int(n)
    if n >=0:
        n_int += 1
    n = input("Inserisci il numero: ")
print(n_int)
    