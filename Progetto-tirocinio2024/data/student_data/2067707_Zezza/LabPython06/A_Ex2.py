s=input('stringa: ')
i=0
f=len(s)-1
liv=0
while i<=int(len(s)+1)/2:
    if s[i]==s[f]:
        liv+=1
        i+=1
        f-=1
    else:
        break
if i>=len(s)/2:
    liv=len(s)
print('livello di palindromicità:',liv)
        
