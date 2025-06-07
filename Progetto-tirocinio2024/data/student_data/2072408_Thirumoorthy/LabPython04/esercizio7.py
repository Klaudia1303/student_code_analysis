s=input('inserire stringa:')
i=0
a=0
c='0'
while i<len(s):
    if s.count(s[i])>a:
        a=s.count(s[i])
        c=s[i]
    elif s.count(s[i])==a:
        c=s[max(s.rfind([i]),s.rfind(c))]
    i+=1
print(c)


