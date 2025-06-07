n=int(input("Inserisci il numeratore "))
d=int(input("Inserisci il denominatore "))
if(n<d):
    print("frazione propria")
elif(n%d==0):
    print("frazione apparente")
elif(n>d&(n%d!=0)):
    print("frazione impropria")
