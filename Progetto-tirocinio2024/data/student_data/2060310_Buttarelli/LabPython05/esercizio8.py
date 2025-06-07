b = int(input("Inserisci la base del triangolo isoscele (maggiore o uguale a tre e dispari): "))
while b < 3 or b % 2 == 0:
    b = int(input("Input non valido. Inserisci la base del triangolo isoscele (maggiore o uguale a tre e dispari): "))
for i in range(b):
    for j in range(b + i):
        if (b - j - 1) > i:
            print(" ", end = "")
        else:
            print("*", end = "")
    print()
        
    
    
