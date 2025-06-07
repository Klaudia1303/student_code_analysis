s = input("Stringa: ")
if len(s) == 0:
    print("input non valido")
elif s[0] == s[-1]:
    print("caratteri iniziale e finale uguali")
else:
    print("caratteri iniziale e finale diversi")
