s=str(input())
p=False
for i in range(0,len(s)):
    if s.count(s[i])>1:
        p=True
print(p)        
