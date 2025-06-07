s=str(input())
i=0
m=0
while i<len(s):
    n=s.count(s[i])
    if n>=m:
        m=n
        d=s[i]
    i=i+1
print(d)    
