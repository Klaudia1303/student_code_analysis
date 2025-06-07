t=float(input("Inserici una tempertura "))
car=input("Inserisci un carattere ")
if(car=="F"):
    t=(t-32)/1.8
    if(t<=0):
        print("solida")
    elif(t>=100):
        print("gassosa")
    else:
        print("liquido")
else:
    if(t<=0):
        print("solida")
    elif(t>=100):
        print("gassosa")
    else:
        print("liquido")
