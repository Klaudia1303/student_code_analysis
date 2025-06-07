t = int(input("Inserisci la temperatura dell'acqua: "))
m = input("Inserisci unità di misura (C o F): ")
if m != "C" and m != "c" and m != "F" and m != "f":
    print("Unità di misura non valida.")
else:
    if m == "C" or m == "c":
        if t <= 0:
            print("Solida.")
        else:
            if t >= 100:
                print("Gassosa.")
            else:
                print("Liquida")
    else:
        if ((t - 32) / 1.8) <= 0:
            print("Solida.")
        else:
            if ((t - 32) / 1.8) >= 100:
                print("Gassosa.")
            else:
                print("Liquida")
