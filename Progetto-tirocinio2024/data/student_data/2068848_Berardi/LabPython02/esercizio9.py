m = int(input("inserisci il mese: "))
if m<1 or m>12:
    print("input non valido")
else:
    a = int(input("inserisci l'anno: "))
    if m == 12:
        m = 1
        a += 1
    else:
        m += 1
    print(m, a)