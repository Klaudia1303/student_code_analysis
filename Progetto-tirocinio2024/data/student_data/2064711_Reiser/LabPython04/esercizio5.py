n=int(input("inserire numero maggiore di 0:"))
m=n
p=1
if n==0 or n==1:
    print(n,"! =",1)
else:
    while n!=0:
        p=p*n
        n-=1
    print(m,"! =",p)
