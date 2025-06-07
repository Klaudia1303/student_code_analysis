n=int(input("Inserisci un numeratore"))
d=int(input("Inserisci un denominatore"))
if n<d:
    print("La frazione è propria")
elif n%d==0:
    print("La frazione è apparente")
else:
    print("La frazione è impropria")
