v1=0
v2=0
day=0
for i in range(1,1000):
    v1=v1+20
    v2=v2+i
    day+=1
    if v2>=v1:
        print(day)
        break
