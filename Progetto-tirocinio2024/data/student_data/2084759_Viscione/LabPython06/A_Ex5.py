s=input("immetti una stringa: ")
cmax=""
nmax=0
for i in range(len(s)):
    c=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            c=c+1
        else:
            break
    if c>=nmax:
        cmax=s[i]
        nmax=c
print(cmax, nmax)
            
