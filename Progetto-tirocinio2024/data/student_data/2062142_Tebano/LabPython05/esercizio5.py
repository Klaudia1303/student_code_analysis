p=False
v=False
while p==False:
    s=str(input())
    n=int(input())
    if len(s)>=2:
        p=True
s=s.lower()     
for i in range(0,len(s)-n-1):
        if ord(s[i])==ord(s[i+n]):
            v=True
            print(s[i])
print(v)   
        
