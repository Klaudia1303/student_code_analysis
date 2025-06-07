s = input("inserisci una stringa: ")

if not s: 
	print("la stringa è vuota...")
else: 
	if s[0] == s[len(s)-1]:
		print("caratteri iniziale e finale uguali")
	else:
		print("caratteri iniziale e finale diversi")