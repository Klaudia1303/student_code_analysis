s=input('Inserire una stringa: ')
livello=0
for i in range (1,(len(s)+1)):
    if s[i-1:i]==s[len(s)-i:len(s)-i+1]:
        livello+=1
    else:
        break
print('Il livello è di:',livello)
