n = int(input("inserisci un n maggiore di 0: "))
i = 1

print("stampo tutti i divisori:")

while (n > i):
	if n % i == 0:
		print(i)
	i += 1 