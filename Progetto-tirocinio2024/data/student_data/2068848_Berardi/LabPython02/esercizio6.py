n = int(input("inserisci il numeratore: "))
d = int(input("inserisci il denominatore: "))
if n<d:
    print("propria")
elif n>=d:
    if n%d == 0:
        print("apparente")
    else:
        print("impropria")