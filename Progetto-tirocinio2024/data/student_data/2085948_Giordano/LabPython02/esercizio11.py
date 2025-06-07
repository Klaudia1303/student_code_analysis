t=int(input("Inserisci una temperatura: "))
if t>30:
    print("Molto caldo")
if t<=30 and t>20:
    print("Caldo")
if t<=20 and t>10:
    print("Gradevole")
if t<=10:
    print("Freddo")