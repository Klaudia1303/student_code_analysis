n = int(input("inserire il numeratore n: "))
d = int(input("inserire il denomnatore d: "))
if (n%d == 0):
    print ("apparente")
elif (n > d):
    print ("impropria")
else:
    print("propria")
