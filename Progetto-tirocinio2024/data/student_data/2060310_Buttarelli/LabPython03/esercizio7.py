c = str(input("Inserisci un carattere: "))
while c == "" or len(c) > 1:
    c = str(input("Input non valido. Inserisci un carattere: "))
s = str(input("Inserisci una stringa: "))
while s == "":
    s = str(input("Input non valido. Inserisci una stringa: "))
while s.count(c) <= 2:
    s = str(input("Inserisci una stringa: "))
    while s == "":
        s = str(input("Input non valido. Inserisci una stringa: "))
print("Numero di", c, " in", s, ":", s.count(c))
