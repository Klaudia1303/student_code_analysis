s=input('Inserire una stringa: ')
palindroma=0
for i in range(0,len(s)):
    if s[i]==s[-i-1]:
        palindroma=palindroma+1
    else:
        break
print(palindroma)
    
