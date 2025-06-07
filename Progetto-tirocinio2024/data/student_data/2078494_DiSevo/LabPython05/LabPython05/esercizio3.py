s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una seconda stringa: ")
s = ''
for i in range(len(s1)):
    if s1[i] not in s2:
       s += s1[i]
print(s)
