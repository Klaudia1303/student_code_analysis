s = input('inserisci una stringa')
c = 0
for i in range(0,len(s)):
    if s[i]==s[len(s)-1-i]:
        c+=1

    else:
        break
print(c)
        
    
        
    
    
    
