v1 = 20
v2 = 1
t1 = v1
t2 = v2
giorni = 1
for x in range(0, 1000):
    if (t2 >= t1):
        break
    t1 += v1
    v2 += 1   
    t2 += v2
    giorni += 1

print(giorni)
