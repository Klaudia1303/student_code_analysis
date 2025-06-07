s = input("Inserisci una stringa: ")
massimo = 0
for i in range (len(s)):
    if s.rfind(s[i]) - s.find(s[i]) > massimo:
        massimo = s.rfind(s[i])- s.find (s[i])
print(massimo)
