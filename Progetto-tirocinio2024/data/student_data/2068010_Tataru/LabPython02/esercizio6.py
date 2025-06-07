n=int(input())
d=int(input())
if (n<d):
    print("propria")
if (n%d==0):
    print("apparente")
if (n>d and n%d!=0):
    print("impropria")
