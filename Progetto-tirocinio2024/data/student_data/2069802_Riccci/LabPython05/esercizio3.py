s1=input("Inserisci stringa --> ")
s2=input("Inserisci seconda stringa --> ")
stringa_finale=""
for i in range(len(s1)):
    if s1[i] not in s2:
        stringa_finale+=s1[i]
print(stringa_finale)
