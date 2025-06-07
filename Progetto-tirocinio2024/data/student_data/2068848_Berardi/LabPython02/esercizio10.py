y_dog = float(input("Inserisci l'età del cane: "))
if y_dog < 0:
    print("input non valido")
elif y_dog <= 2:
    print (10.5*y_dog)
else:
    print (10.5*2 + (y_dog-2)*4)