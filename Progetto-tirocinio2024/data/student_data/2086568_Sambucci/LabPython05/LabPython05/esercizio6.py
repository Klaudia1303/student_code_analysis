s=input('Inserire stringa: ')
d=0
maxd=0
for i in range(len(s)):
    if s.count(s[i])>=2:
        d=abs(s.find(s[i])-s.rfind(s[i]))
        if d>maxd:
            maxd=d
print(maxd)
        
