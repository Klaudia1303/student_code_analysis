t=float(input("Inserisci un valore: "))
scala=ord(input("Inserisci la scala utilizzata tra F(Fahrenheit) e C(Celsius): "))
if scala==ord("F"):
    t=float(t-273)
if t<=0:
    print("solida")
elif t>=100:
    print("gassosa")
else:
    print("liquida")
      
