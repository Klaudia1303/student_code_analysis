print("inserisci due stringhe della stessa lungheza")
s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")
frase = ""

for i in range(len(s1)):
    frase += str(s1[i])
    frase += str(s2[i])

print(frase)
    
print(list(range(len(s1)+1)))
