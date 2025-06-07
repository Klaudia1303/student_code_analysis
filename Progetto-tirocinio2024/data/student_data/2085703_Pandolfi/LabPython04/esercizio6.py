n1 = int(input("inserisci primo intero: "))
n2 = int(input("inserisci secondo intero: "))
n3 = n1

while n2 > 1:
	n1 += n3
	n2 -= 1

print(n1)