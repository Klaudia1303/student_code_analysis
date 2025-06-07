n=int(input("Inerisci un numeratore: "))
d=int(input("Inerisci un denominatore: "))

if(n<d):
    print("La frazione e' propria")
elif(n%d==0):
    print("La frazione e' apparente")
elif(n>d and n%d!=0):
    print("La frazione e' impropria")