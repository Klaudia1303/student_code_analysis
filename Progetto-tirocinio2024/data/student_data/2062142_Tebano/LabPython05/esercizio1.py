p=True
while p==True:
    s=input()
    t=input()
    if len(s)==len(t):
        p=False
w=''
for i in range(0,len(s)):
    w=w+s[i]+t[i]
print(w)    
    

