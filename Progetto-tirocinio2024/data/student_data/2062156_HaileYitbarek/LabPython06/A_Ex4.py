k=int(input('inserire 20 o numero maggiore di 0: '))
a=1
d=0
for i in range(1,1001):
    if k*i!=a+d:
        d=d+a
        a=a+1
    else:
        break
print(i)
