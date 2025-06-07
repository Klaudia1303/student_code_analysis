n = int(input("inserisci un numero maggiore o uguale a 2: "))

if n < 2: 
	print("numero non valido")
	exit()
	
for x in range(n):
	for y in range(n):
		if x == 0 or x == n-1:
			print("*", end="")
		else:
			if y == 0 or y == n-1:
				print("*", end="")
			elif y == x or y == (n-1) - x:
				print("*", end="")
			else: print(" ", end="")		
	print("")
