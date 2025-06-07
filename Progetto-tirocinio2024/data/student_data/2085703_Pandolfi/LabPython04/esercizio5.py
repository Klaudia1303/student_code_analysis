n = int(input("inserisci un intero >= 0: "))
i = 1

while n > 1:
	i *= n
	n -= 1

print(i)