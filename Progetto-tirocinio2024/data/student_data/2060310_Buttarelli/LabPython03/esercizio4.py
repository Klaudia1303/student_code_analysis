x = int(input("Inserisci un numero x compreso tra 0 e 10: "))
while x < 0 or x > 10:
    x = int(input("Input non valido. Inserisci un numero x compreso tra 0 e 10: "))
y = int(input("Inserisci un numero y compreso tra 0 e 10: "))
while y < 0 or y > 10:
    y = int(input("Input non valido. Inserisci un numero y compreso tra 0 e 10: "))
i = 1
while i <= 10:
    if i != x and i != y:
        print(i, "\n")
    i += 1
