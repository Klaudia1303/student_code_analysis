c=input("inserisci un carattere: ")
s=input("Inserisci una stringa: ")
while s.count(c)<=2:
    s=input("inserisci stringa: ")
print("il carattere è presente "+str(s.count(c))+" volte")
