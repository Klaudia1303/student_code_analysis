s = input("inserisci una frase: ")
n = int(input("Inserisci un numero: "))
frase = ""
for i in range(len(s)):
    aggiunta = s[i]*n
    frase += aggiunta
print(frase)
