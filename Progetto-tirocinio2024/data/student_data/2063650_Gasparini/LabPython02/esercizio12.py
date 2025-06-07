t = float(input("Temperatura: "))
scala = input("Scala: ")
if scala != "C" and scala != "F":
    print("input non valido")
else:
    if scala == "F":
        t = (t - 32)/1.8
    if t <= 0:
        print("solida")
    elif t < 100:
        print("liquida")
    else:
        print("gassosa")
