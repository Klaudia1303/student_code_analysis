n=int(input("Inserisci numeratore: "))
d=int(input("Inserisci denominatore: "))
if n>=d:
    if n%d==0:
        print("apparente")
    elif n%d!=0:
        print("impropria")
else:
    print("propria")
