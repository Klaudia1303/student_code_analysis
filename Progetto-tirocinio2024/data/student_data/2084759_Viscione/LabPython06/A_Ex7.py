s1=input("immetti prima stringa: ")
s2=input("immetti seconda stringa: ")

lmax=0
smax=""
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        if len(s1[i:])<lmax:
            break
        elif s2.find(s1[i:j])!=-1 and len(s1[i:j])>=lmax:
            smax=s1[i:j]
            lmax=len(s1[i:j])
            
print(smax)
