s1 = input("inserisci una stringa: ")
s2 = input("inserisci una stringa: ")

for x in s1:
	if s2.find(x) == -1:
		print(x, end="")
