s=input("Inserire una stringa: ")
lunghezza=0
livello=0
i=len(s)-1
for x in range(len(s)):
    if s[x]==s[i]:
        livello+=1
        i-=1
    else:
        break
print("La stringa ",s," è di livello: ",livello)