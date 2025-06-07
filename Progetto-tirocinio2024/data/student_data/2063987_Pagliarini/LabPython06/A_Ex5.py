s=input()
c=1
a1=''
m=0
for i in s:
    if a1==i:
        c+=1
        if c>=m:
        
            m=c
            t=i
    else:
        c=0
    
    
    a1=i
    
print(t,' ',m+1)
