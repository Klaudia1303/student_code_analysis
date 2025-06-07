v1 = float(input("Velocità 1: "))
v2 = float(input("Velocità 2: "))

d1 = 0
d2 = 0
for i in range(1, 1001):
    d1 += v1
    d2 += v2 * i
    if d2 >= d1:
        print(i)
        break
    
