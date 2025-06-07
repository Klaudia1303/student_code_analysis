c = input('Inserisci carattere: ')

i = 0
while i<1:
	s = input("Inserisci stringa: ")
	count = 0
	index = 0
	while index < len(s):
		if s[index] == c:
			count += 1
		index += 1
	if count > 2:
		print(count)
		i += 1
