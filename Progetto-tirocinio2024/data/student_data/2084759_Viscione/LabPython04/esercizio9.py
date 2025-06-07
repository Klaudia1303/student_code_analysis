n=int(input("immetti un intero maggiore di 0: "))
i=1
s=0
p1=1
p2=0
while i<=n:
    s=p1+p2
    print(s)
    p1=p2
    p2=s
    i+=1
