n=float(input("immetti il numeratore: "))
d=float(input("immetti il denominatore: "))
if n<d:
    print("propria")
elif n%d==0:
    print("apparente")
elif n>d and n%d!=0:
    print("impropria")
