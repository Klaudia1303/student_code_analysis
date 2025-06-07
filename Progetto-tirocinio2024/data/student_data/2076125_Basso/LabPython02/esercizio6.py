

n=int(input("Inserire nominatore:\t"))
d=int(input("Inserire denominatore (diverso da zero):\t"))
if n%d==0:
    print(n,"/",d,"è apparente")
elif n<d:
    print(n,"/",d,"è propria")
else:
    print(n,"/",d,"è impropria")
