s: int = 1
n: int = 0
while s != 0:
    s: int = int(input('numero: '))
    if s % 3 == 0:
        n += s
print(n)