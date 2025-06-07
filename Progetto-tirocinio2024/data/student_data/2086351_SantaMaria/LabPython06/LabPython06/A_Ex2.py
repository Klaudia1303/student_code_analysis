s=input('Inserire una stringa: ')
livello=0
k=len(s)-1
i=0
while i!=len(s) or k!=-1:
    if s[i]==s[k]:
        livello+=1
        k-=1
        i+=1
    elif s[i]!=s[k]:
        break
print(livello)
