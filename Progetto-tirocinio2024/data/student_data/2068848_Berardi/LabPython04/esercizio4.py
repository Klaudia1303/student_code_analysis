n = input("Inserisci il numero: ")
tot = 0
while n != "0":
    n = int(n)
    if n%3==0:
        tot += n
    n = input("Inserisci il numero: ")
print(tot)