s=input("Inserisci una stringa ")
if(s!=""):
    if(s[0]==s[(len(s)-1)]):
        print("caratteri iniziale e finale uguali")
    else:
        print("caratteri iniziale e finale diversi")
