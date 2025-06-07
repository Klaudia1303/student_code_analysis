s = input("inserisci una stringa non vuota: ")

livello = 0
m = int(len(s)/2)

for x in range(m):
	# print(s[x])
	# print("--", s[-x-1])
	if s[x] == s[-x-1]:
		livello += 1
	else:
		break;

if (livello == m):
	livello = len(s)

print(livello)