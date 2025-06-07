s=input('inserisci una stringa palindroma')
check=True
i=0
livello=0
while check:
    if s[i]==s[len(s)-i-1]:
        check=True
        livello+=1
        i+=1
    else:
        check=False

print(livello)
    
