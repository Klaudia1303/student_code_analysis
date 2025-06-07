s=input("inserisci stringa: ")
occ=1
c=""
massimo=0
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        occ+=1
    else:
        if massimo<=occ:
            massimo=occ
            c=s[i]
            occ=1
print(c, massimo)
