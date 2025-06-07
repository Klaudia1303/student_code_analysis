s1 = input("Inserisci la prima stringa: ")
while s1 == "":
    s1 = input("Input non valido. Inserisci la prima stringa: ")
s2 = input("Inserisci la seconda stringa (di lunghezza pari alla stringa precedente): ")
while s2 == "":
    s2 = input("Input non valido. Inserisci la seconda stringa (di lunghezza pari alla stringa precedente): ")
while len(s1) != len(s2):
    print("Le due stringhe devono avere la stessa lunghezza.")
    s1 = input("Inserisci la prima stringa: ")
    while s1 == "":
        s1 = input("Input non valido. Inserisci la prima stringa: ")
    s2 = input("Inserisci la seconda stringa (di lunghezza pari alla stringa precedente): ")
    while s2 == "":
        s2 = input("Input non valido. Inserisci la seconda stringa (di lunghezza pari alla stringa precedente): ")
for i in range(0, len(s1)):
               print(s1[i], s2[i], sep = "", end = "")
               
