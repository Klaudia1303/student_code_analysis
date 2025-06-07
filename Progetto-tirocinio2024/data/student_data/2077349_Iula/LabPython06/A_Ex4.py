v1=20
v2=1
for t in range(1,1000):
    s1=v1*t
    s2=(1/2)*t**2+v2*t
    if s1==s2:
        print(t+1)
        break
