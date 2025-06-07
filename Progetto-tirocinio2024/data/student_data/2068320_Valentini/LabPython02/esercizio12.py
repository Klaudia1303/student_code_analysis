temp=int(input("Inserire il valore della temperatura: "))
s=str(input("Inserire l'iniziale della scala che si vuole utilizzare - C=Celsius, F=Fahrenheit: "))
if s=="F" or s=="f":
    t=(temp-32)/1.8
else:
    t= temp
if (t>=100):
    print("Gassosa")
elif (t<100) and (t>0):
    print("Liquida")
else:
    print("Solida")









