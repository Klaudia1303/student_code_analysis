s = str(input("inserisci una stringa non vuota: "))
if s[0] == s[len(s)-1]:
    print("caratteri iniziale e finale uguali")
else:
    print("caratteri iniziale e finale diversi")