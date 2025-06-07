x=int(input("Inserisci il numero di un mese: "))
y=int(input("Inserici un anno: "))
z=x+1
w=y+1
if (x>12 or x<1):
    print("Input non valido")
else:
    if z==13:
        print(1,w)
    else:
        print(z,y)
    