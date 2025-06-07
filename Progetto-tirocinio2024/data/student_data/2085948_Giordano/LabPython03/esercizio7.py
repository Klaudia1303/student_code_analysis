from xml.dom.pulldom import CHARACTERS


c=(input("Inserisci un carattere: "))
s=str(input("Inserisci una stringa: "))
while s.count(c) <3:
    s=str(input("Inserisci una stringa: "))
else:
    print(c,"é contenuta in ",s,s.count(c)," volte")