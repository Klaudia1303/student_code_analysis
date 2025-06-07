s=input("Inserisci stringa: ")
massimo=0
for i in range(0,len(s)):
    distanza=s.rfind(s[i])-i
    if distanza>massimo:
        massimo=distanza
print(massimo)
