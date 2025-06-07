i1=0
i2=0
g=0
for i in range(1000):
    i1+=20
    i2+=i
    g+=1
    if i1==i2:
        break
print('giorni impiegati',g)
