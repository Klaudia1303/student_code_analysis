n1 = int(input("inserisci un numero maggiore di 0: "))
n2 = int(input("inserisci un numero maggiore di 0: "))


for x in range(int(n1-2)):
	d = n1 - x
	if n1 % d == 0 and n2 % d != 0:
		print(d)