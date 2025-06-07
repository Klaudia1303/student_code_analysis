e = int(input("inserisci età cane: "))
e2 = float(0)

if e < 0:
	print("età non valida")
else:
	if e > 0 and e < 3:
		e2 = e * 10.5
	if e > 2: 
		e2 = ((e -(e-2)) * 10.5) + ((e-2) * 4) 
	print(e2)