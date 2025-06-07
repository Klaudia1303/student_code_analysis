s1 = input("inserisci una stringa: ")
s2 = input("inserisci una stringa: ")
s = s1
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            s = s.replace(s1[i], "")
print(s)

