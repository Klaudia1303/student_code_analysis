s=input('inserisci stringa')
c=False
for i in range (len(s)):
    for j in range (i+1,len(s)):
        if s[i]==s[j]:
            c=True

print(c)

        
