s = input("inserisci una stringa: ")
n = int(input("inserisci un intero n: "))

for x in range(len(s)):
	print(s[x]*n, end="")