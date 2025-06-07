s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")

for i in range(len(s1)):
    m = s1.replace(s1[i],"",i)
print(m)
