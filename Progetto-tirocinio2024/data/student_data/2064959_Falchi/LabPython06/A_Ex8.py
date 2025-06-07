s1 = input("Inserire prima stringa: ")
s2 = input("Inserire seconda stringa: ")
n = int(input("Inserire un numero intero: "))

sF = ""

for i in range(len(s1)):
	if s1[i] in s2:
		for j in range(len(s2)):
			if s2[j] == s1[i] and abs(j-i) <= n:
				sF += s1[i]
				s2[j].replace(s2[j], " ")

print(sF)