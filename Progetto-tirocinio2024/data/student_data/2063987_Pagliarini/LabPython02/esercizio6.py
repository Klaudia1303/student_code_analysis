n=int(input("inserisci un numero"))
d=int(input("inserisci un numero"))

if(d>n):
    print("propria")
elif(n%d==0):
    print("apparente")
elif(n%d!=0) and (n>d):
    print("impropria")
