n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

result = 0

if n2 > 0:
    for i in range(n2):
        result += n1
elif n2 < 0:
    for i in range(n2, 0):
        result -= n1

print(result)
