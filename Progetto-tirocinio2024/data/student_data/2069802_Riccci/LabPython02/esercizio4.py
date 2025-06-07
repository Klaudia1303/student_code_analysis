s = input("Inserisci stringa --> ")
while(len(s)==0):
    s = input("Inserisci stringa non vuota --> ")
if(s[0]==s[-1]):
    print("Carattere iniziale e finale uguale")
else:
    print("Carattere iniziale e finale diversi")
