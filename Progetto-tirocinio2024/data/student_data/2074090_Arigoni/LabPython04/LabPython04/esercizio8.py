s=input("inserisci una stringa (stringa vuota per terminare): ")

while s != " ":
    precedente = s
    s=input("inserisci una stringa (stringa vuota per terminare): ")
    if precedente[-1] in s[0]:
        print(precedente, " ", s)
