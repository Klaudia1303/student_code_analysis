n=int(input('inserire un intero maggiore di 0:'))
a=0
b=1
c=a+b
print(b)
while b<=n:
    print(c)
    a=b
    b=c
    c=a+b
