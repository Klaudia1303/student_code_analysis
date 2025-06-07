print("ESERCIZIO 11: inserita una temperatura (numero intero), \
riporti un messaggio che indichi se è caldo oppure freddo\n")
t=int(input("Inserisci la temperatura: \t"))
if t>30:
    print("Molto caldo")
elif t<=30 and t>20:
    print("Caldo")
elif t<=20 and t>10:
    print("Gradevole")
elif t<=10:
    print("Freddo")
