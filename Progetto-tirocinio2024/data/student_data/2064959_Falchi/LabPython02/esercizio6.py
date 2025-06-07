n = int(input("Inserire valore numeratore: "))
d = int(input("Inserire valore denominatore: "))

if n < d:
    print("La frazione è propria.")
elif n == d*2:
    print("La frazione è apparente.")
elif n > d and not n == d*2:
    print("La frazione è impropria.")
