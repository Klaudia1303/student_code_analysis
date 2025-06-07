s=input("inserisci una stringa: ")
while len(s)==0:
    s=input("Reinserisci la stringa: ")
if s[0]==s[len(s)-1]:
    print("I caratteri iniziale e finale sono uguali")
else:
    print("I caratteri iniziale e finale sono diversi")
