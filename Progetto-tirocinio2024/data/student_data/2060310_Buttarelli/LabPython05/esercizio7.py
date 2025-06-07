s = input("Inserisci una stringa: ")
while s == "":
    s = input("Input non valido. Inserisci una stringa: ")
controllo = "False"
for c in s:
    if s.find(c) != s.rfind(c):
        controllo = "True"
print(controllo)
