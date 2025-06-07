s=str(input("inserire una stringa:"))
t=len(s)
b=0
c=""
for i in range(0,t):
    a=0
    for l in range(i,t-1):
        if s[i]==s[l]:
            a+=1
        b=max(a,b)
        if b==a:
            d=s[i+l]
        if s[i]!=s[l]:
            break
        
print(d,'    ',b)
