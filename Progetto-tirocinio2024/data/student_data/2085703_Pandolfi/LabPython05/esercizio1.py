s1 = input("inserisci una stringa: ")
s2 = input("inserisci una stringa con stessa lunghezza della precedente: ")

if len(s1) != len(s2):
	print("le due stringhe hanno lunghezza diversa")
	exit()

for x in range(len(s1)):
	print(s1[x] + s2[x], end="")
