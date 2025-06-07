s=input('inserire stringa: ')
i=0
j=len(s)-1
while i<j:
    if s[i]==s[j]:
        i +=1
        j -=1
    else:
        print('palindromo di livello: ',i)
        break
if s[i]==s[j]:
    print('palindromo di livello: ',len(s))
        
    
