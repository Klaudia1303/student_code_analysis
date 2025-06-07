import math

n = int(input("inserisci la base del triangolo (n. dispari / uguale a 3): "))

if n % 2 == 0: 
	print("numero non valido")
	exit()

c = math.ceil(n/2) 
q = 1

for x in range(1, c+1):
	print(" "*(c-(x)), end="")
	print("*" * q)
	q = q + 2
