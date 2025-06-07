n = int(input("inserisci un numero maggiore di 1: "))

i = 1
n1 = 2

while n1 < n: 
	while i < n1:
		if n1 % i == 0 and n1 != i and n1 != 2:
			break
		i += 1
	if i == n1:
		print(i)
	n1 += 1
	i = 2

