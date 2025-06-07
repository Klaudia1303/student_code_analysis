n1 = 0
n2 = 0
z = 0
for i in range(1,1000):
    n1 = n1+i
    n2 = n2+20
    z=z+1
    if n2 == n1:
        break
print(z)
