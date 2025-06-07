n=int(input("scrivi numeratore: "))
d=int(input("scrivi denominatore: "))
if n<d:
    print("la frazione è propria")
if d%n==0:
    print("la frazione è apparente")
elif n>d and n%d!=0:
    print("la frazione è impropria")
