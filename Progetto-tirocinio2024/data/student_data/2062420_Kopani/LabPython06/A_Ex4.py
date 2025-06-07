v1=20
d2=0
for i in range(1,1001):
    d1=v1*i
    d2=d2+i
    if d1==d2:
        break
print('Il secondo viaggiatore raggiungerà il primo in',i,'giorni')