n=-1
while n<0:
    n=int(input('Inserire un intero maggiore o uguale a 0: '))
r=n-1
if n==0 or n==1:
    print(1)
else:
    while n>1 and r>=1:
        n=n*r
        r=r-1
    print(n)
