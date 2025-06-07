s01=0
s02=0
j=1
for i in range(1,10001):
    s1=20
    distanza1=s1+s01
    s01=distanza1
    s2=i
    distanza2=s2+s02
    s02=distanza2
    if distanza1==distanza2:
        break
print(i)
