n = input("inserisci il valore del numeratore: ")
n = int(n)
d = input("inserisci il valore del denominatore: ")
d = int(d)

if n<d:
    print("propria")
elif (n%d) == 0:
    print("apparente")
else:   print("impropria")    
    
