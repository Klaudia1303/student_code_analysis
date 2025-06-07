s=input('inserire stringa: ')
x=0
for i in range(0,len(s)):
    if s.count(s[i])>=x:
        x=s.count(s[i])
        lettera=s[i]
print(lettera,s.count(s[i]))
