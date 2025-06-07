s1=input("Inserisci prima stringta: ")
s2=input("Inserisci seconda stringa: ")
lmax=0
smax=''
for i in range(len(s1)):
    stringa=''
    for j in range(i,len(s1)):
        stringa +=s1[j]
        if s2.find(stringa)!=-1:
            if lmax<len(stringa):
                smax=stringa
                lmax=len(stringa)
print(smax)
