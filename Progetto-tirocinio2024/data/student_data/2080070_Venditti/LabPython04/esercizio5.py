n=int(input('inserire un intero maggiore o uguale a 0: '))
c=n-1
a=c*n
while n>1:
    c-=1
    a=a*c
    if c==1:
        print(a)
if n==0 or n==1:
    print(1)

