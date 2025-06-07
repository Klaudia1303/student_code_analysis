v1=0
v2=0
for i in range (1,1000):
    v2+=i
    v1+=20
    if(v2==v1):
        print(i)
        break
