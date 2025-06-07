n=int(input('inserire un intero maggiore o uguale a 0: '))
if n>=2:
    i=n-1
    x=n
    while i>1:
        x=x*i
        i=i-1
    print(x)
else:
    print(1)
