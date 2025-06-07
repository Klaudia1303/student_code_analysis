s=input("inserisci una stringa alfanumerica")
c=1
r=0
for i in range(len(s)):
    if i==len(s)-1:
        break
    elif s[i]==s[i+1]:
        c+=1
        if c>=r:
            r=c
            t=s[i]
    else:
        c=1
print(t,r)
