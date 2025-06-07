s1 = str(input("Inserisci una stringa: "))
while s1 == "":
    s1 = str(input("Input non valido. Inserisci una stringa: "))
s2 = str(input("Inserisci una stringa: "))
while s2 == "":
    s2 = str(input("Input non valido. Inserisci una stringa: "))
s3 = str(input("Inserisci una stringa: "))
while s3 == "":
    s3 = str(input("Input non valido. Inserisci una stringa: "))
while (len(s1) + len(s2)) != len(s3):
    s1 = s2
    s2 = s3
    s3 = str(input("Inserisci una stringa: "))
    while s3 == "":
        s3 = str(input("Input non valido. Inserisci una stringa: "))
print(s1, s2, s3)
