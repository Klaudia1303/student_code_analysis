s=input("inserisci una stringa:")
check=False
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            check=True
print(check)
