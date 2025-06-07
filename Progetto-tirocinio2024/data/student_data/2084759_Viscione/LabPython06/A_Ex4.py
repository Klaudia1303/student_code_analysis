v1=int(input("immetti velocita' primo viaggiatore: "))
v2=int(input("immetti velocita' iniziale secondo viaggiatore: "))
k1=0
k2=0
for i in range(1,1001):
    k1=k1+v1
    k2=k2+v2*i
    if k2>=k1:
        break
print(i)
    
