s = str(input("Inserisci una stringa (inserire tutti caratteri alfabeici minuscoli per terminare): "))
while s == "":
    s = str(input("Input non valido. Inserisci una stringa (inserire tutti caratteri alfabeici minuscoli per terminare): "))
while s.isalpha() and not s.islower():
    s = str(input("Inserisci una stringa (inserire tutti caratteri alfabeici minuscoli per terminare): "))
    while s == "":
        s = str(input("Input non valido. Inserisci una stringa (inserire tutti caratteri alfabeici minuscoli per terminare): "))
    print("Primo carattere dell'ultima stringa: ", s[0])
    print("Ultimo carattere dell'ultima stringa: ", s[len(s) - 1])

    
