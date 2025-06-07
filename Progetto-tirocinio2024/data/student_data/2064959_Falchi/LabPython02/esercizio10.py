DogAge = float(input("Inserire età del cane: "))
ManAge = 0

if DogAge > 0:
    if DogAge <= 2:
        ManAge = 10.5*DogAge
        print("Età corrispondente dell'uomo:", ManAge)
    elif DogAge > 2:
        ManAge = 10.5*2
        ManAge = ManAge + 4*(DogAge-2)
        print("Età corrispondente dell'uomo:", ManAge)
else:
    print("ERRORE! Età inserita non valida.")
