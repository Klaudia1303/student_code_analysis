s=input("Inserisci una stringa: ")
conta=0
j=''
for i in range(len(s)):
    if(i+1<len(s)):
        if(s[i]==s[i+1]):
            j=s[i]
            conta=s.count(j)
print(j)
print(conta)