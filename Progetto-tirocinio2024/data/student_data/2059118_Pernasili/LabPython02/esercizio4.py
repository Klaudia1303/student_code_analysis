s = input("Inserisci una stringa s non vuota: ")
if len(s) == 0:
    print("Errore")
else:
    a = s[0]
    b = s[len(s)-1]
if a == b:
    print("caratteri iniziale e finale uguali: ")
elif a!= b:
    print("caratteri iniziale e finale diversi: ")
