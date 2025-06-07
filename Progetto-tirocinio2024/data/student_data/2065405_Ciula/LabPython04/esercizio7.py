s=input("Inserisci una stringa: ")
i=0
M=s.count(s[0])
c=0
while(i<=len(s)-1):
    if(s.count(s[i])>M):
        M=s.count(s[i])
        c=i
    elif(s.count(s[i])==M):
        if(s[i]==s[len(s)-1]):
            M=s.count(s[i])
            c=i
    i+=1
print(s[c])
