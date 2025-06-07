i=0
g=0
c=1
v1=0
v2=0
for i in range(1,1000):
    g+=1
    v1+=20
    v2+=c
    c+=1
    if(v1==v2):
        break
print(g)
        
