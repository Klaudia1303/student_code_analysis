s1 = input("inserisci una stringa: ")
s2 = " "

while s2[0] != s1[-1]:
	s1 = s2
	s2 = input("inserisci una stringa: ")

print(s1, " ", s2)