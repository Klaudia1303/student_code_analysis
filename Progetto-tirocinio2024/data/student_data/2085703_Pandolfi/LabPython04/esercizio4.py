i = 0

n = input("inserisci un intero: ")

while int(n) != 0:
	if int(n) % 3 == 0:
		i += 1
	n = input("inserisci un intero: ")

print(i)