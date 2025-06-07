s = input("inserisci una stringa: ")

d = 0

for x in range(len(s)):
	n = s.rfind(s[x])
	if s[x] != -1 and (n - x) > d:
		d = n - x

print(d)