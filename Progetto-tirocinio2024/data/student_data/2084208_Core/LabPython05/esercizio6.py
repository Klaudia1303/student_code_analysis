s=input('Inserire una stringa: ')
uguali=False
for i in range(0,len(s)):
    u=len(s)-1
    while u!=i and not uguali:
        if s[i]==s[u]:
            uguali=True
            differenza=abs((u-i))
        else:
            uguali=False
            differenza=0
        u-=1
print(differenza)


        
            
