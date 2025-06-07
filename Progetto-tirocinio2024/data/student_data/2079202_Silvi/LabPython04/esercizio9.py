n=int(input("inserire un numero maggiore di 0:"))
n1=1
n2=2
ns=0
for i in range(0,n):
    if i!=0:
        print(n1)
        ns=n1+n2
        n1=n2
        n2=ns
    else:
        print(n1)
