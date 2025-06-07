numero1 = int(input("Inserisci numero1: "))
numero2 = int(input("Inserisci numero2: "))

for i in range(1, numero1+1):
    if (numero1 % i == 0 and numero2 % i != 0):
        print(i)
