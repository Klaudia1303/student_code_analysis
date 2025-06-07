s = ""
i = 0

while s.find("c") == -1 or s.find("a") == -1:
	s = input("inserisci una stringa: ")
	i += 1

print(i)