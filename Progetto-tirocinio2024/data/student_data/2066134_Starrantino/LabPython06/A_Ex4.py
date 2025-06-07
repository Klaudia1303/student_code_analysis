v1: int = 20
d1, d2 = 0, 0
for day in range(1, 1001):
    d1 += v1
    d2 += day
    if d1 == d2:
        print(day)
        break
    