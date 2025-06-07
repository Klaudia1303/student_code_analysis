n = input("Inserisci il numeratore: ")
n = int(n)
d = input("Inserisci il denomiatore: ")
d = int(d)
if n > d and n % d != 0:
    print("Impropria.")
else:
    if n % d == 0:
        print("Apparente.")
    else:
        print("Propria.")
