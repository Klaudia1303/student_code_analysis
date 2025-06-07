v1=0
v2=0
i=0
for g in range(1,1000):
    v1+=20
    i+=1
    v2+=i
    if v1==v2:
        print(g)
        break
