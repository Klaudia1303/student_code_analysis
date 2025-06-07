s=input('inserire una stringa:' )
x=0
i=0
if s!='':
    while i<len(s):
        if s.count(s[i])>=x:
            x=s.count(s[i])
            p=i
        i+=1
print(s[p])
