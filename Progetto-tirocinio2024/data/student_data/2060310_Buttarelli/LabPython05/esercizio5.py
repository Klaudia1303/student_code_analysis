s = input("Inserisci una stringa di almeno 2 caratteri: ")
while len(s) < 2:
    s = input("Input non valido. Inserisci una stringa di almeno 2 caratteri: ")
n = int(input("Inserisci un numero positivo: "))
while n <= 0:
    n = int(input("Input non valido. Inserisci un numero positivo: "))
controllo = "False"
for i in range(0, len(s)):
    if (i + n) < len(s):
        if s[i] == s[(i + n)]:
            controllo = "True"
print(controllo)
