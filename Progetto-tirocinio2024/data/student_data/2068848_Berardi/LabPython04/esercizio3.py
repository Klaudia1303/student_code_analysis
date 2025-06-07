n = input("Inserisci il numero: ")
tot = 0
while n != "*":
    n = int(n)
    if n<0:
        tot += n
    n = input("Inserisci il numero: ")
print(tot)