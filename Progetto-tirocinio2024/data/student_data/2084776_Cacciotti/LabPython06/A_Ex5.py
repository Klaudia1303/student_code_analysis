s= input('inserire una stringa non vuota')
mas=0
contm=''

for i in range (len(s)):
    if s.count(s[i])>=mas and s[i] not in contm:
        mas=s.count(s[i])
        contm=s[i]
print(contm, mas)

    
