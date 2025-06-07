s = str(input("Inserisci una stringa: "))
while s == "":
    s = str(input("Input non valido. Inserisci una stringa: "))
i = 0
massimo = 0
lmassima = 0
while i < len(s):
    if s.count(s[i]) >= massimo:
        lmassima = s[i]
        massimo = s.count(s[i])
    i += 1
print("Lettera che compare più volte in ", s,": ", lmassima)
    
