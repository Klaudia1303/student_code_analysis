temp=float(input("Inserisci la temperatura"))
if temp<=10:
    print("Freddo")
elif temp>10 and temp<=20:
    print("Gradevole")
elif temp>20 and temp<=30:
    print("Caldo")
else:
    print("Molto caldo")
