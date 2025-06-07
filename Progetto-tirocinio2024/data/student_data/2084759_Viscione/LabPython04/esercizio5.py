n=int(input("immetti un intero maggiore o uguale a 0: "))
f=1
i=n
while i>0 and i<=n and n!=0 and n!=1:
    f=f*i
    i-=1
print(f)
