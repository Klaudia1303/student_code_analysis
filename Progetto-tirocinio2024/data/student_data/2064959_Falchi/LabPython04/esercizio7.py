s = input("Inserire una stringa: ")

ricorrenze = 0
carattere1 = None

ambiguità = False
carattere2 = None

i = 0
    
while i < len(s):
		if s.count(s[i]) > ricorrenze:
			ricorrenze = s.count(s[i])
			carattere1 = s[i]
		elif s.count(s[i]) == ricorrenze:
		      	#print('Ricorrenza trovata!')
		      	ambiguità = True
		      	carattere2 = carattere1
		      	carattere1 = s[i]
		
		i += 1

if ambiguità:
    print(s[max(s.rfind(carattere1), s.rfind(carattere2))])