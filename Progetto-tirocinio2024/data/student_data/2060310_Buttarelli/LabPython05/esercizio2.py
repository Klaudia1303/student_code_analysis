s = input("Inserisci una stringa: ")
while s == "":
    s = input("Input non valido. Inserisci una stringa: ")
n = int(input("Inserisci un numero positivo: "))
while n <= 0:
    n = int(input("Input non valido. Inserisci un numero positivo: "))
for i in range(0, len(s)):
    print(s[i] * n, sep = "", end = "")
