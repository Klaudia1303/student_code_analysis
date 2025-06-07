t = input("inserisci la temperatura: ")
t = float(t)
scala = input("inserisci C (Celsius) o F (Fahrenheit): ")

if scala == "F":
        t = (t - 32)/1.8
        
if scala == "C" or scala == "F":
    if t <= 0:
        print("solida")
    elif 0 < t < 100:
        print("liquida")
    elif t <= 100:
        print("gassosa")       

if scala != "C" and scala != "F":
    print("input non valido")
              
