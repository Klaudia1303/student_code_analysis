i = 0

n = input("inserisci un intero: ")

while n != "*":
	if int(n) <= 0:
		i += 1
	n = input("inserisci un intero: ")

print(i)