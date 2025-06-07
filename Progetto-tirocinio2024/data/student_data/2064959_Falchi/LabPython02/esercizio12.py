t = int(input("Inserire temperatura: "))
tipo_conversione = input("Opzioni di conversione disponibili:\n\n\tF) Da Celsius a Farenheit\n\tC) Da Farenheit a Celsius.\n\nSi prega di scegliere il tipo di conversione: ")

risultato = 0

if tipo_conversione.lower() == "f":
    print("Tipo di conversione scelto: da Celsius a Farenheit.\n")
    
    risultato = (t - 32)/1.8
    print("°F =", risultato)

    if t<= 0:
        print("Stato acqua: solido.")
    elif t>=100:
        print("Stato acqua: gassoso.")
    else:
        print("Stato acqua: liquido.")
    
elif tipo_conversione.lower() == "c":
    print("Tipo di conversione scelto: da Farenheit a Celsius.\n")

    risultato = (0 * 9/5) + 32
    print("°C =", risultato)

    if risultato <= 0:
        print("Stato acqua: solido.")
    elif risultato >=100:
        print("Stato acqua: gassoso.")
    else:
        print("Stato acqua: liquido.")
    
else:
    print("ERRORE! Parametro di conversione non valido.")
