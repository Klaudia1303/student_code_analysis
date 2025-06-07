s1 = ""
s2 = ""
s = None

MemAddress = 1
Corr_Trovata = False

while not Corr_Trovata:
	s = input("Inserire stringa: ") 
	if (len(s) == len(s1) + len(s2)) and (s1 != "" and s2 != ""):
		Corr_Trovata = True
	else: #Memorizza la stringa nella variabile sovrascritta meno recentemente.
		if MemAddress == 1:
			s1 = s
			MemAddress = 2
		else:
			s2 = s
			MemAddress = 1
				
print(s1, s2, s)