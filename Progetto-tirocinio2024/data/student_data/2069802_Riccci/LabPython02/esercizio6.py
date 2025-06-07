n = int(input("Inserisci numeratore --> "))
d = int(input("Inserisci denominatore --> "))
if(n<d):
    print("Frazione propria ")
elif(n%d==0):
    print("Frazione apparente")
else:
    print("Frazione impropria")
