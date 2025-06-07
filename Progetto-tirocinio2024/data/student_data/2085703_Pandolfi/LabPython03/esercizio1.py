def stampa_numeri(n):
	print(n)
	if n > 2:
		stampa_numeri(n-2)

n = int(input("inserisci un numero n: "))

if n <= 2: 
	exit()
elif n % 2 != 0:
	n = n - 1

stampa_numeri(n)



