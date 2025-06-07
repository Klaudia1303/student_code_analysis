n = int(input("numeratore: "))
d = int(input("denominatore: "))
if n % d == 0:
    print("frazione apparente")
else:
    if n > d:
        print("frazione impropria")
    else:
        print("frazione propria")
