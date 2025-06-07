c=input("Inserisci un carattere: ")
s=input("Inserisci stringa: ")
while s.count(c)<=2:
    s=input("Inserisci stringa: ")
print("Il carattere compare",s.count(c),"volte")
