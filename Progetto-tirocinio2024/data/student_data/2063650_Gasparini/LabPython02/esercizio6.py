numer = int(input("Numeratore: "))
denom = int(input("Denominatore: "))
if numer < denom:
    print("propria")
elif numer % denom == 0:
    print("apparente")
else:
    print("impropria")
