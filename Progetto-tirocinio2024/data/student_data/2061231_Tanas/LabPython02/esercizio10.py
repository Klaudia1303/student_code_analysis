c = float(input("età cane: "))
if c < 0:
    print("input non valido")
else:
    if c <= 2:
        eta = c*10.5
    else:
        eta = (2*10.5) + (c-2)*4
    print("L'età del cane in anni umani è " + str(eta))
