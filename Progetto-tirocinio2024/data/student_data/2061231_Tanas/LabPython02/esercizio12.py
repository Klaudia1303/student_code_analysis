t = int(input("temperatura: "))
scala = input("scala (C o F): ")
if scala != 'C' and scala != 'F':
    print("scala non valida")
else:
    if scala == 'F':
        temp = (t-32)/1.8
    else:
        temp = t
    if temp <= 0:
        print("solida")
    elif 0 < temp < 100:
        print("liquida")
    elif temp >= 100:
        print("gassosa")

            
