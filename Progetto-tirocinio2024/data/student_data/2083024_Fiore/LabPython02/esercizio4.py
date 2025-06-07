s = input("inserisci una stringa: ")

if s == "":
    print("la stringa è vuota")
elif s[0] == s[-1]:
    print("caratteri iniziale e finale uguali")
else:
    print("caretteri iniziale e finale diversi")
