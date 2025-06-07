s=input('Inserisci una stringa: ')
corretto=True
i=0
livello=0
while corretto:
    if s[i]==s[len(s)-i-1]:
        corretto=True
        i+=1
        livello+=1
    else:
        if s==s[::-1]:
            livello=len(s)
        corretto=False
        
print(livello)
