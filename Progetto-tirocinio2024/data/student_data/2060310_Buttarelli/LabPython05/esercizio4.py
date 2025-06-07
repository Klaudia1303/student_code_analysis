n1 = int(input("Inserisci il primo numero positivo: "))
while n1 <= 0:
    n1 = int(input("Input non valido. Inserisci il primo numero positivo: "))
n2 = int(input("Inserisci il secondo numero positivo: "))
while n2 <= 0:
    n2 = int(input("Input non valido. Inserisci il secondo numero positivo: "))
for i in range(n1, n2, n1):
    print(i)
