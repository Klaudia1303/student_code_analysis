n: int = int(input('numero: '))
v1, v2 = 0, 1
temp: int = 0
print(1)
while n > 1:
    print(v1 + v2)
    temp = v2
    v2 = v2 + v1
    v1 = temp
    n -= 1