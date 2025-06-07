s1 = input("inserisci una stringa con almeno 2 caratteri: ")

if len(s1) < 2:
	print("stringa troppo piccola")
	exit()

n = int(input("inserisci un intero n: "))

flag = False

for x in range(len(s1) - n):
	if s1[x] == s1[x+n]:
		flag = True

print(flag)