s=input()
m=0
a=''
for i in range(0,len(s)):
    if s.count(s[i])>=m:
        m=s.count(s[i])
        a=a+s[i]
print(a[-1],s.count(a[-1]))        
    
    

