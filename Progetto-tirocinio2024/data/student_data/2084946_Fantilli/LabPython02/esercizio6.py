n = input('numeratore: ')
n = int(n)
d = input('denominatore: ')
d = int(d)
print("la frazione", str(n)+"/"+str(d), "è:")
if n < d :
    print("propria")
elif n%d == 0 :
    print("apparente")
else :
    print("impropria")
