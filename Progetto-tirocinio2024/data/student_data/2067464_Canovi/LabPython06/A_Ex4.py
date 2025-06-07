vel1 = 20
vel2 = 1
spazio1 = 0
spazio2 = 0

for i in range(1, 1001):
    spazio1 = spazio1 + vel1
    spazio2 = spazio2 + vel2
    if spazio1 == spazio2:
        print(i)
        break
    vel2 += 1
