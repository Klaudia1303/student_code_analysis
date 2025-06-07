t=int(input("Inserisci la temperatura: "))
if t>30:
    print("molto caldo")
elif 20<t<=30:
    print("caldo")
elif 10<t<=20:
    print("gradevole")
else:
    print("freddo")
