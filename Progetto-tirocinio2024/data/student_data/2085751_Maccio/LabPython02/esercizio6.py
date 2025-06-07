n=int(input("Inserire il numeratore:   "))
d=int(input("Inserire il denominatore:   "))
if n<d:
    print("La frazione",n,"/",d,"è propria")
elif n%d==0:
    print("La frazione",n,"/",d,"è apparente")
elif n>d and n%d!=0:
    print("La frazione",n,"/",d,"è impropria")
    
