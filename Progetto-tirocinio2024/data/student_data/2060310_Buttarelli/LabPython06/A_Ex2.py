s = input("Inserisci una stringa: ")
while s == "":
    s = input("Input non valido. Inserisci una stringa: ")
livello = 0
for i in range(len(s) // 2):
    if s[i] == s[-(i + 1)]:
        livello += 1
    else:
        break
if livello == (len(s) // 2):
    print("Livello di palindromicità di ", s, ": ", len(s), sep = "")
else:
    print("Livello di palindromicità di ", s, ": ", livello, sep = "")
