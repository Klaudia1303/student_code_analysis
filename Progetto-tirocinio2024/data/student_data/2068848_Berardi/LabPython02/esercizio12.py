u = str(input("inserisci l'unità di misura (F)(C): "))
t = int(input("inserisci la temperatura: "))
if u == "F":
    t = (t-32)/1.8
if t>=100:
    print("Gassosa")
elif t<=0:
    print("Solida")
else:
    print("Liquida")
    