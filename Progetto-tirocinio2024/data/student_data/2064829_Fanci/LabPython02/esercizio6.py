n = int(input("inserisci numeratore: "))
d = int(input("inserisci denominatore: "))
if n<d:
    print("frazione propria")
elif n%d==0:
    print("frazione apparente")
elif n>d:
    print("frazione impropria")
