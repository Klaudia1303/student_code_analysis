temp=int(input("inserisci una temperatura: "))
if temp>30:
    print("Molto caldo")
elif temp<=30 and temp>20:
    print("Caldo")
elif temp<=20 and temp>10:
    print("Gradevole")
if temp<10:
    print("Freddo")
