s = input("inserisci una stringa: ")
i = 1
c = s[i]

while i < len(s):
	if s.count(s[i]) >= s.count(s[i-1]):
		c = s[i]
	i += 1

print(c)