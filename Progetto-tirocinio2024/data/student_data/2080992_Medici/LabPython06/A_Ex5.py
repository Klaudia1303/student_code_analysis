s=str(input('inserire una stringa: '))
mas=0
l=''
for i in range(len(s)):
    ll=s[i]
    mass=0
    for j in range(len(s)-i):
        if ll==s[i+j]:
            mass+=1
        else:
            break
    if mass>=mas:
        mas=mass
        l=ll
print(l,mas)
