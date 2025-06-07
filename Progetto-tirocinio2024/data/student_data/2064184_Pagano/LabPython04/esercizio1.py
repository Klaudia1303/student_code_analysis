s = input("Inserisci una stringa: ")
i = 1

while s.find("a") == -1 or s.find("c") == -1:
    s = input("Inserisci una stringa: ")
    i += 1

print(i)
