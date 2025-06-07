c = input("Inserisci un carattere --> ")
s = input("Inserisci una stringa --> ")
while(s.count(c)<=2):
    s = input("Inserisci una stringa --> ")
print("Il carattere "+str(c)+" compare ",s.count(c)," volte")
