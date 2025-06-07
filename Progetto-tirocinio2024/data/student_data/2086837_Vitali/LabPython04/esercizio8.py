s=input("Inserisci stringa s: ")
c=s[-1]
s=input("Inserisci stringa s: ")
while s[0]!=c:
    appo=s
    c=s[-1]
    s=input("Inserisci stringa s: ")
print(appo,s)
