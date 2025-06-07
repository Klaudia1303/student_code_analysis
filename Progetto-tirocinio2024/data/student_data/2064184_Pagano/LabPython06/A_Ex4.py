v1 = 20
v2 = 0

d1 = 0
d2 = 0

for i in range(1, 1001):
    v2 += 1
    
    d1 += v1
    d2 += v2

    if d2 >= d1:
        print(i)
        break
