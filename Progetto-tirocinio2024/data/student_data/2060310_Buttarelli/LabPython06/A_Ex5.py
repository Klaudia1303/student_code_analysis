s = input("Inserisci un stringa: ")
while s == "":
    s = input("Input non valido. Inserisci un stringa: ")
contatore = 1
carattere = 0
ripetizione = 0
for i in range(len(s)):
    if i == len(s) - 1:
        break
    else:
        if s[i] == s[(i + 1)]:
            carattere = s[i]
            contatore += 1
        else:
            ripetizione = contatore
            contatore = 1
print("Carattere: ", carattere, ", Ripetizioni: ", ripetizione, sep = "")
