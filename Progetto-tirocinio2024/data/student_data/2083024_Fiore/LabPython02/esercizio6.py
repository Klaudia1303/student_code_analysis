n = int(input("inserisic numeratore: "))
d = int(input("inserisci denominatore: "))
if n < d :
    print("La frazione è una frazione propria")
elif n % d == 0 :
    print("la frazione è una frazione apparente" )
elif n > d :
    print("la prazione è una frazione impropria")
