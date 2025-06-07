g = 0
for i in range(1000):
    g += 1
    v2 = 20*g
    v1 = ((1+g)*g)//2
    if v1 == v2:
        break
print("Giorno: ",g)
