dogAge = input("inserisci l'età del cane: ")
dogAge = float(dogAge)

if dogAge <=2:
    print(dogAge*10.5)
elif dogAge > 2:
    print(2*10.5 + (dogAge - 2)*4)
