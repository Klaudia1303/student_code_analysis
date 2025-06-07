s1 = input("inserisci una stringa non vuota: ")
s2 = input("inserisci una stringa non vuota: ")

sub = ""

for x in range(len(s1)):
	for y in range(len(s1)+1):
		if s1[x:y] in s2 and len(s1[x:y]) > len(sub):
			sub = s1[x:y]

print(sub)