n=int(input("inserisci il valore del numeratore:"))
d=int(input("inserisci il valore del denominatore:"))
if n<d:
    print("propria")
elif n % d ==0:
    print("apparente")
elif n>d and n%d != 0:
    print("impropria")
