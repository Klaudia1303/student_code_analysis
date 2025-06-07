print("Inserire una stringa contenente almeno due caratteri ed un intero positivo")
s=input("Inserire la stringa:")
n=int(input("Inserisci un numero:"))
while len(s)<2 or n<1:
    print("La stringa inserita non contiene almeno due caratteri oppure il numero inserito non è positivo/nInserire la stringa ed il numero:")
    s=input("stringa:")
    n=int(input("numero:"))
i=0
F=False
while i < (len(s)-n) and not F:
    if s[i]==[i+n]:
        F=True
    i+=1
print(F)
