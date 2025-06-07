v1 = 20
v2 = 1

d1 = 20
d2 = 1
giorni = 1
for i in range(1000):
    if d2 != d1:
        giorni += 1
        d1 += 20
        v2 += 1
        d2 += v2
    else:
        break
    
print(giorni)
    
    
