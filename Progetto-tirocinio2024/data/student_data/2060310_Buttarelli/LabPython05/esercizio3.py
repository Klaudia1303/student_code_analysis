s1 = input("Inserisci la prima stringa: ")
while s1 == "":
    s1 = input("Input non valido. Inserisci la prima stringa: ")
s2 = input("Inserisci la seconda stringa: ")
while s2 == "":
    s2 = input("Input non valido. Inserisci la seconda stringa: ")
for c in s1:
    if c not in s2:
        print(c, sep = "", end = "")
