k=20
a=1
d=0

for i in range(1,1001):
    if k*i!=a+d:
        d=d +a
        a=a+1
        print(d)
    else:
        break
print(i)
