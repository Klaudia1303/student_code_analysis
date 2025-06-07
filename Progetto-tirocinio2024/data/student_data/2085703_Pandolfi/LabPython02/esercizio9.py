m = int(input("inserisci mese: "))
a = int(input("inserisci anno: "))

if m < 12:
	m += 1
elif m == 12:
	m = 1
	a += 1 
else:
	print("input non valido")
	exit()

print(m, " ", a)