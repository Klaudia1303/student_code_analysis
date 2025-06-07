v1=20
v2=0
for i in range(1,1000):
    v2+=i
    v1=20*i
    if v2>=v1:
        break
print(i)
