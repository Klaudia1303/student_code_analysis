n1 = int(input("Inserisci il primo numero positivo: "))
while n1 <= 0:
    n1 = int(input("Input non valido. Inserisci il primo numero positivo: "))
n2 = int(input("Inserisci il secondo numero positivo: "))
while n2 <= 0:
    n2 = int(input("Input non valido. Inserisci il secondo numero positivo: "))
print("Divisori di ", n1," non comuni con quelli di ", n2, ": ", sep = "")
for i in range(n1, 1, -1):
    if n1 % i == 0 and n2 % i != 0:
        print(i)
