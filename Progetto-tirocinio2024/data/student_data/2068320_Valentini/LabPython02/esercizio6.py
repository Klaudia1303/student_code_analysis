n=input("Inserire il nominatore: ")
d=input("Inserire il denominatore: ")
app=int(n)%int(d)
if int(n)<int(d):
    print("La frazione è propria")
elif int(app)==0:
    print("La frazione è apparente")
else:
    print("La frazione è impropria")
