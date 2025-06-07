print("ESERCIZIO 5: inserimento di un anno e verifica che sia un anno bisestile")
anno=int(input("Inserisci un anno per verificare che sia bisestile: "))
if (anno%4==0 and anno%100!=0) or (anno%400==0):
    print("Anno bisestile")
else:
    print("Anno non bisestile")
