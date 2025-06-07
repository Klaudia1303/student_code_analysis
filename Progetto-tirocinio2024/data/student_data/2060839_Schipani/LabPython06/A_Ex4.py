v1=int(input('km al gg viaggiatore 1 '))
d1=v1
v2=1
for i in range(2,1001):
    d1+=v1
    v2+=i
    if v2>=d1:
        break
print('giorni trascorsi: ',i)
