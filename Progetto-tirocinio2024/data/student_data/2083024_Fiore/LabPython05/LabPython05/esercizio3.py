s1 = input("inserisci una frase: ")
s2 = input("inserisci una frase: ")
frase = ""

lista = []
for v in range(len(s2)):
        lista += s2[v]
for i in range(len(s1)):
    if s1[i] not in lista:
        frase += s1[i]
print(frase)
