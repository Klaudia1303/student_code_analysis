s=input('Inserire una stringa (palindroma):')
p=0
for i in range(len(s)):
    if s[i]==s[len(s)-i-1]:
        p+=1
    else:
        break
print('Il livello di palindromicità della stringa è =',p)
    
    
    
