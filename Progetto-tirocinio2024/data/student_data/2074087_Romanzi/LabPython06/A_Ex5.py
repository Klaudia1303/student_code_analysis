k=True
while k:
    s=str(input('Stringa '))
    if len(s)!=0:
        k=False
    else:
        print('Stringa vuota')
c=1
r=1
f=''
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        for j in range(i,len(s)):
            if s[j]==s[j-1]:
                c=c+1
            else:
                break
        if c>=r:
            f=s[i]
            r=c
        c=1
print(f,r)
