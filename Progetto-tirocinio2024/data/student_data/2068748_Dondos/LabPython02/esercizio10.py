age = float(input("Inserisci età del cane: "))
if 0<=age<=2:
    print(10.5*age)
if age>=2:
    print(10.5*2+4*(age-2))
if age<0:
    print("input non valido")
