s=input("inserisci stringa: ")
pal=0
for i in range(0,len(s)):
    if s[i]==s[len(s)-1-i]:
        pal=1+i
    else:
        break
print("livello: ",pal)
        
