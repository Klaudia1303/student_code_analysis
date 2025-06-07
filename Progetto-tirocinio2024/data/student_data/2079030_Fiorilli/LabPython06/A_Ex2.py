s=input('inserisci una stringa: ')
livello=0
for i in range (len(s)):
    if s[i]==s[len(s)-1-i]:
        livello+=1
    else:
        break
print (livello)
