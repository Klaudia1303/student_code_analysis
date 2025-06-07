n=int(input("Inserisci un numeratore: "))
d=int(input("Inserisci un denominatore: "))
if n<d:
    print("frazione propria")
elif n>d and n%d!=0:
    print("frazione impropria")
if (n%d)==0:
        print("frazione apparente")
