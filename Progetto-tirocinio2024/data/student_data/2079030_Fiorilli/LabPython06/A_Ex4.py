v1=20
v2=1
km2=0
km1=0
for g in range (1,1001):
    km1+=v1
    km2+=g
    if km1<=km2:
        break
print (g)
