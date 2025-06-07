e=float(input("immetti l'eta' del cane: "))
if e>0:
    if e>2:
        c=21+(e-2)*4
    else:
        c=10.5*e
    print(c)
else:
    print("input non valido")
