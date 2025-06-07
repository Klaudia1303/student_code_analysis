s=input('inseire una stringa: ' )
nl=0
nc=0
l=0
c=0
tl=''
i=0
for i in s1:
    for c in range(len(s1)):
        if i==s[c:c+1]:
            nl=i
            nc+=1
    if (nc>=l):
        l=nc
        tl=nl
    nc=0
    nl=''
print(l,tl)
