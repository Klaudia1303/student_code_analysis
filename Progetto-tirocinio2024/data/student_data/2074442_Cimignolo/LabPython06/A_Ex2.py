s=input('inserisci una stringa: ')
livello=0

if s[:]==s[::-1]:
    print(len(s))
else:
    for i in range(len(s)//2):
        if (s[i]!=s[len(s)-1-i]):
            break
        livello+=1
        
    print(livello)
        
