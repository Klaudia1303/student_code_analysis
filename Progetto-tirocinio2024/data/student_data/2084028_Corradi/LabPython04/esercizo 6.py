x=int(input('numero intero 1'))
y=int(input('numero intero 2'))
z = False
if x<0:
    x = abs(x)
    z = True
if y<0:
    y = abs(y)
    if z:
        z = False
    else:
        z = True
tot = 0
while x>0:
    tot += y
    x -= 1
if z:
    tot *= -1
print(tot)
