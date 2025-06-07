s1 = input("inerisci prima stringa: ")
s2 = input("inserisci seconda stringa: ")
c=""
for i in range (len(s1)):
    for j in range (len(s2)):
        if s1[i]==s2[j]:
            c=c+(s1[i])
            break
print(c)
