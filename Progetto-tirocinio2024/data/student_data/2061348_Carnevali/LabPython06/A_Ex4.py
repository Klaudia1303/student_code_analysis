s1=int(0)
s2=int(0)
v2=int(1)
while s1!=s2 or v2==1:
    s1=s1+20
    s2=s2+v2
    v2=v2+1
print(v2-1)
s1=int(0)
s2=int(0)
v2=int(1)
for m in range(1000):
    s1=s1+20
    s2=s2+v2
    v2=v2+1
    if s1==s2:
        print(v2-1)
        break
