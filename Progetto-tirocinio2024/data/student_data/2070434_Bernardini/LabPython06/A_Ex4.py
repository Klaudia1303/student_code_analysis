x=int(input('inserire prima vel: '))
y=int(input('inserire seconda vel: '))
b=int(y)
a=int(x)
for i in range(1000):
    x=x+a
    y=y+b
    b=b+1
    if y>=x:
        break
print(i)
