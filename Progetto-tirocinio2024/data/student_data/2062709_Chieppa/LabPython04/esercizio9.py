n=int(input('inseire intero positivo: '))
x=0
y=1
z=0
i=2
print('1','\n'+'1')
while i<=n:
    z=x+y
    x=y
    y=z
    i=i+1
    print(x+y,'\n')
