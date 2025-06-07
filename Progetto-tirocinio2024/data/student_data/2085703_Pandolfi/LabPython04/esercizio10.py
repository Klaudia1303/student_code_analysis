s1 = input("inserisci una stringa: ")
s2 = input("inserisci una stringa: ")
s3 = input("inserisci una stringa: ")

while ((len(s1) + len(s2)) != len(s3)) and ((len(s2) + len(s3)) != len(s1)) and ((len(s3) + len(s1)) != len(s2)):
	s1 = s2 
	s2 = s3
	s3 = input("inserisci una stringa: ")

print(s1, " ", s2, " ", s3)