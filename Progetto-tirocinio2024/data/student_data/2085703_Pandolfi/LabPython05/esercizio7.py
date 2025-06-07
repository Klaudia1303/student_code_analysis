s = input("inserisci una stringa: ")

flag = False

for x in range(len(s)):
	if s.count(s[x]) > 1:
		flag = True
		
print(flag)