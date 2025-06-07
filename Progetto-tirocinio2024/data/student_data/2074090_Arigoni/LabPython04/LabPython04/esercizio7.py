s=str(input('Stringa '))
p=0
k=''
for i in range(0,len(s)):

    if s.count(s[i])>p:
        p=s.count(s[i])
        k=s[i]
print(str(p)+' '+k)
