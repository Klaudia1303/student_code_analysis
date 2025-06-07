s=input("Inserisci stringa --> ")
while(len(s)==0):
    s=input("Input non valido, inserisci una stringa --> ")
i=0
while(i<len(s) and ord(s[i])<=100):
    i+=1
if i>=len(s):
    print("stringa conusmata, carattere non trovato")
else:
    print("Il primo carattere con codice Unicode maggiore di 100 è ",s[i])
