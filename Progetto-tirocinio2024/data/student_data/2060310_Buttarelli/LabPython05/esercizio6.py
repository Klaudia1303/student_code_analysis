s = input("Inserisci una stringa: ")
while s == "":
    s = input("Input non valido. Inserisci una stringa: ")
distmax = 0
for c in s:
    if (s.rfind(c) - s.find(c)) >= distmax:
        distmax = s.rfind(c) - s.find(c)
print("Distanza massima:", distmax)
