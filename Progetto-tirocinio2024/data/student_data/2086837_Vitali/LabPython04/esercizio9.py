n=int(input("Insersici numero n maggiore di 0: "))
p=1
s=1
if n==1:
    print("\n",p)
elif n==2:
    print("\n",p)
    print("\n",s)
else:
    print("\n",p)
    print("\n",s)
    for i in range(n-2):
        fibbo=p+s
        print("\n",fibbo)
        p=s
        s=fibbo
