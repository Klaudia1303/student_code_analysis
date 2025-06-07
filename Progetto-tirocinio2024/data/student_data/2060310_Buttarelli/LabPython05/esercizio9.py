l = int(input("Inserisci il valore del lato del quadrato (maggiore o uguale a tre e dispari): "))
while l < 3 or l % 2 == 0:
    l = int(input("Input non valido. Inserisci il valore del lato del quadrato (maggiore o uguale a tre e dispari): "))
for i in range(l):
    for j in range(l):
        if i == 0 or i == (l - 1) or j == 0 or j == (l - 1):
            print("*", end = "")
        else:
            print(" ", end = "")
    print()
