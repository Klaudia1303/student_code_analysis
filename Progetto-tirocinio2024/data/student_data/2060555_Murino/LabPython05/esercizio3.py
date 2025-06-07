s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
s=str()
i=0

for c in s1:
    if c not in s2:
        s=(s+c)
        i+=1
print(s)
