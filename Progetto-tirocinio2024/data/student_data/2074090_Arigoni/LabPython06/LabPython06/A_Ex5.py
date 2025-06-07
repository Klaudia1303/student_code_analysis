s=str(input("Inserisci una stringa>> "))
c=1
r=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        for j in range(i,len(s)):
            if s[j]==s[j-1]:
                c=c+1
            else:
                break
        if c>=r:
            r=c
            f=s[i]
        c=1
print(r,f)

