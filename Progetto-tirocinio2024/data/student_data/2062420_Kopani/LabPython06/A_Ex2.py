s=input('Inserire una stringa: ')
l=0
for i in range(len(s)):
    if s[i]==s[len(s)-1-i]:
        l+=1
    else:
        break
print('Il livello di palindromicità è',l)