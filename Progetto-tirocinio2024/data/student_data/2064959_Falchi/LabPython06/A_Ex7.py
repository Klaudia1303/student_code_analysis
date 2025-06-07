s1 = input("Inserire prima stringa: ")
s2 = input("Inserire seconda stringa: ")

maxSeq = None
maxRec = 0

for i in range(len(s1)):
	for j in range(len(s1)):
		if s1[i:j] in s2:
			if len(s1[i:j]) >= maxRec:
				maxSucc = s1[i:j]
				maxRec = len(s1[i:j])

print(maxSucc)