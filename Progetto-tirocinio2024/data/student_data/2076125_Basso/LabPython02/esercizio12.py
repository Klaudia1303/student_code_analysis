

t=float(input("Inserire temperatura dell'acqua:\t"))
T=input("Inserire F per la scala Fahrenheit o C per la scala Celsius:\t")

f=(t-32)/1.8

if T=="C":
    if t<=0:
        print("solida")
    elif t>=100:
        print("gassosa")
    else:
        print("liquida")

elif T=="F":
    if f<=0:
        print("solida")
    elif f>=100:
        print("gassosa")
    else:
        print("liquida")

else:
    print("Attento, non hai inserito una scala giusta.\nRicordati di scrivere F o C maiuscole.")
    
