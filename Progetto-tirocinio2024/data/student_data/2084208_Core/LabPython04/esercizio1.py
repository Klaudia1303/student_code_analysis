s='stringa'
i=0
c=0
a=0
conto=0
while c+a!=2:
    i=0
    s=input('Inserisci una stringa: ')
    conto=conto+1
    while i<len(s):
        if s[i]=='c':
            c=1
        if s[i]=='a':
            a=1
        i=i+1
print(conto)
