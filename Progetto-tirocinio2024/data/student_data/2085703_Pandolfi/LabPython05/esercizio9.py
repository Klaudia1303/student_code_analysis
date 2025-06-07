n = int(input("inserisci il lato del quadrato (n. dispari maggiore o uguale a 3): "))

if n % 2 == 0: 
	print("numero non valido")
	exit()

for x in range(n):
	if x == 0 or x == n-1:
		print("*" * n)
	else:
		print("*" + " "*(n-2) + "*")