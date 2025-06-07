s1 = input("Inserisci la prima stringa: ")
while s1 == "":
    s1 = input("Input non valido. Inserisci la prima stringa: ")
s2 = input("Inserisci la seconda stringa: ")
while s2 == "":
    s2 = input("Input non valido. Inserisci la seconda stringa: ")
sequenza = ""
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            sequenza += s1[i]
        else:
            break
print(sequenza)
