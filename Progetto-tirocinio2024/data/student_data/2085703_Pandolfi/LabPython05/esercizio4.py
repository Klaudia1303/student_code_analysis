n1 = int(input("inserisci un intero: "))
n2 = int(input("inserisci un intero: "))

for x in range(int(n2/n1)):
	n = n1*(x+1)
	if (n < n2):
		print(n)
