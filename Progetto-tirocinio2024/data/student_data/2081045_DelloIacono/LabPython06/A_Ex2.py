s=input('inserire una stringa: ')
cont=0
for i in range (len(s)):
    if (s[i]==s[len(s)-1-i]):
        cont=cont+1
    else:
        break
    
print('livello: ',cont)
