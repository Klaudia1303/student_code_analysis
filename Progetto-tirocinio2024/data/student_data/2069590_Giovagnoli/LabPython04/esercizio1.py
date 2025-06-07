s = input("Inserire una stringa: ")
contatore=0
if not s.count("a") or not s.count("c"):
    contatore+=1
while not s.count("a") or not s.count("c"):
    s = input("Inserire una stringa: ")
    contatore +=1
print("Il numero di stringhe è: ",contatore)