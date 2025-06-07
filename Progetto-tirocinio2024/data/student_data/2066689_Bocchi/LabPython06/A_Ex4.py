v1= 20
v2= 1
for i in range(1,1000):
    v1 = 20*i
    v2 = v2 + i
    if v2 >= v1:
        print(i)
        break
