s=input("Inserire una stringa")
p=0
for i in range(len(s)):
    if(s[i]==s[(len(s)-1)-i]):
        p+=1
    else:
        break
print("La palindromicità è di",p,"livello")
