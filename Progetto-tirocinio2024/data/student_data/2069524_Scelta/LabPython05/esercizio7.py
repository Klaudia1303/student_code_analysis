s=str(input("Inserisci una stringa:"))
risultato=False
for i in s:
    if s.count(i)>1:
        risultato=True
    else:
        risultato=False
print(risultato)
