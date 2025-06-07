l = int(input("Inserisci il valore del lato del quadrato (maggiore o uguale a 2): "))
while l < 2:
    l = int(input("Input non valido. Inserisci il valore del lato del quadrato (maggiore o uguale a 2): "))
d = l - 1
for i in range(l):
    for j in range(l):
        if i == 0 or i == (l - 1) or j == 0 or j == (l - 1) or i == j or j == d:
            print("*", end = "")
        else:
            print(" ", end = "")
    d -= 1
        
    print()
