temp=int(input("Inserisci una temperatura: "))
tipo=input("Inserisci un tipo di temperatura: ")
if tipo=="F" or tipo=="f":
    temp=(temp-32)/1.8
if temp>=100:
    print("Gassosa")
elif temp<100 and temp>0:
    print("Liquida")
else:
    print("Solida ")
    
