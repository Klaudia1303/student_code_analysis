s = str(input("Inserisci una stringa: "))
while s == "":
    s = str(input("Input non valido. Inserisci una stringa: "))
stringhe = 1
while s.find("a") == -1 or s.find("c") == -1:
    s = str(input("Inserisci una stringa: "))
    stringhe += 1
print("Numero di stringhe inserite:", stringhe)
