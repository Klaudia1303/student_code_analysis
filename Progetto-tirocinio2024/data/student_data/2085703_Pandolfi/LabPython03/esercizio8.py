s = input("inserisci una stringa palindroma: ")

while s != s[len(s)::-1]:
	s = input("stringa non palindroma, inserisci una stringa palindroma: ")

print("stringa palindroma di lunghezza ", len(s))