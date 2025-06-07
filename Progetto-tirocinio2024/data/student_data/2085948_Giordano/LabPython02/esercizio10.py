h_age = int(input("Inserisci l'età di un cane: "))

if h_age < 0:
	print("Deve essere un numero positivo :(.")
	exit()
elif h_age <= 2:
	d_age = h_age * 10.5
else:
	d_age = 21 + (h_age - 2)*4

print("L'età del cane in anni umani è:", d_age)

  