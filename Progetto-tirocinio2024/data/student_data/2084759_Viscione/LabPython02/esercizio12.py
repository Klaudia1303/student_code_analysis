t=float(input("immetti la temperatura: "))
print("C=Celsius F=Fahrenheit")
s=input("immetti la scala tramite un carattere: ")
if s=="C" or s=="F":
    if s=="F":
        t=(t-32)*5/9
    if t<=0:
        print("solida")
    elif t>=100:
        print("gassosa")
    else:
        print("liquida")
else:
    print("scala non valida!")
