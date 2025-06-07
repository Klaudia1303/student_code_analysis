temperatura = float(input("Inserisci la temperatura: "))
if temperatura<=10:
    print("freddo")
elif 10<temperatura<=20:
    print("gradevole")
elif 20<temperatura<=30:
    print("caldo")
else:
    print("molto caldo")
