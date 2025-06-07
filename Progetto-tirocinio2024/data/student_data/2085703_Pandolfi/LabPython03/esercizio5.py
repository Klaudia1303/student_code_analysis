s = "333rdam"
while (s.islower() == False) or (s.isalpha() == False):
	s = input("inserisci una stringa non vuota: ")
	print(s[0], "",s[len(s)-1])