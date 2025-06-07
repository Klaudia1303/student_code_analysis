s = input('insrisci una stringa: ')
livello = 0
for i in range(len(s)):
       if s[i] == s[-i-1]:
            livello +=1
       else:
            break
print(livello)
        
            
    
        
       

    
