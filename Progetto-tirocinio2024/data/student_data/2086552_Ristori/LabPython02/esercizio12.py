var1=float(input("Inserire il valore della temperatura:"))
c=str(input("Inserire l'unità di misura(F o C):"))
if c==str("C"):
    print("La scala selezionata è quella Celsius")
    if var1<=0:
        print("solida")
    elif 0<var1<100:
        print("liquida")
    elif var1>=100:
        print("gassosa")
elif c==str("F"):
    print("La scala selezionata è quella Fahrenheit")
    if var1<=32:
        print("solida")
    elif 32<var1<212:
        print("liquida")
    elif var1>=212:
        print("gassosa")
        
