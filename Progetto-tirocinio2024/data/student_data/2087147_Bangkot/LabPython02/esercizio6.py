n=int(input())
d=int(input())
if n<d:
    print("propria")
elif n%d==0:
    print("apparente")
elif n>d:
    print("impropria")
