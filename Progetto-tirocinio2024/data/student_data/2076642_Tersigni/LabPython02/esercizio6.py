n=int(input("nominatore"))
d=int(input("denominatore"))
if n<d :
    print("propria")
elif n%d==0 :
    print("apparente")
elif n>d and n%d==1 :
    print("impropria")


            
