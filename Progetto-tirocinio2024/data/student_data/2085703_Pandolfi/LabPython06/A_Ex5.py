s = input("inserisci una stringa alfanumerica non vuota: ")

c = ""
n = 0

for x in range(len(s)):
	for y in range(x, len(s)):
		if x == y and s[x] != s[y]:
			break
		if s[x] == s[y] and n <= y-x+1:
			n = y-x+1
			c = s[x]
print(c, n)
