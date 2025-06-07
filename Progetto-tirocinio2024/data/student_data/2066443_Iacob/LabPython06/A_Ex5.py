s = input('Insert string: ')
n=1
m=1
c = s[len(s)-1]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        n=n+1
        if n>=m:
            m = n
            c = s[i]
    else:
        n=1
print(c,m)
