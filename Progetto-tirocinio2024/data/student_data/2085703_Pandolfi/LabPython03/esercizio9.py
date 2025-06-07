n = int(input("inserisci un numero: "))
i = 2

while i < n**1/2:
	if n % i == 0 and n != i:
		print("numero non primo")
		exit()
	i += 1

print("numero primo")