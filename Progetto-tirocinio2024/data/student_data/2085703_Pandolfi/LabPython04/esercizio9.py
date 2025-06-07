n = int(input("inserisci un numero > 0: "))

n1 = 1
n2 = 1

print(n1)

while n > 1:
	print(n2)
	n3 = n2
	n2 = n1 + n2
	n1 = n3
	n -= 1
