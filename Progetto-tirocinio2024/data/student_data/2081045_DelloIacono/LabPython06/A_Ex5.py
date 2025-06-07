s=input('inserire alfanumerico: ')
mass=0
cmax=""
for i in range (len(s)):
    if(s.count(s[i])>=mass):
        mass=s.count(s[i])
        cmax=s[i]
print(cmax, s.count(cmax))
