b=True
while b:
    s=input("Inserire una stringa che contenga almeno 2 caratteri: ")
    if len(s)>=2:   b=False
    else:   print("\n\t\tLa stringa non contiene almeno 2 caratteri\n")
b=True
while b:
    n=int(input("Inserire un numero intero positivo: "))
    if n>0:   b=False
    else:   print("\n\t\tIl numero non è positivo (>0)\n")
b=False
for i in range(len(s)):
    if (i+n)<len(s):
        if s[i]==s[i+n]:    b=True; break
print("Compaiono 2 lettere uguali a distanza del numero inserito?",b)
