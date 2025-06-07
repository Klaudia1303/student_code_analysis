t = int(input("Inserisci la temperatura: "))
if t > 30:
    print("Molto caldo ")
elif t > 20 and t <= 30:
    print("Caldo ")
elif t > 10 and t <= 20:
    print("Gradevole ")
elif t <= 10:
    print("Freddo ")
