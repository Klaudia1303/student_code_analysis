s = input('Inserisci una stringa: ')
livello = 0

for i in range(0,len(s)):
    
    if s[i] == s[(len(s)-1)-i]:
        print(s[i],s[len(s)-1-i])
        livello+=1
    else:
        break
    
print(livello)
    
