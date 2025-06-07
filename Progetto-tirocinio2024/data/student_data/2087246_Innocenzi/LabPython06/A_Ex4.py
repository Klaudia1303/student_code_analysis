v1=20
v2=0
km1=0
km2=0
for i in range(1, 10001):
    km1+=v1
    v2+=1
    km2+=v2
    if(km2==km1):
        print(i)
        break
    