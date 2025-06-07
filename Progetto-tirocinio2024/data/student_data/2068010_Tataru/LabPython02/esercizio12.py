t=int(input("Inserisci la temperatura "))
q=input("Inserisci F per Fahrenheit o C per Celsius ")
if (q=="C"):
    if (t<=0):
        print("solida")
    elif (t<100):
        print("liquida")
    else:
        print("gassosa")
else:
    if (t<=32):
        print("solida")
    elif (t<212):
        print("liquida")
    else:
        print("gassosa")
