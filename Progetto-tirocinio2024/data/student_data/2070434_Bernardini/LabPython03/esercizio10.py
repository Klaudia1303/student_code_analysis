n=0
while n<=1:
    n=int(input('inserire num. maggiore di 1'))
k=2
x=2
while k<=n:
    if k%x==0 and x!=k:
        x=1
        k=k+1
    elif x>k:
        print(k)
        x=1
        k=k+1
    x=x+1

