s=input("Inserisci una stringa:")
finale=s[len(s)-1]
c=True
while c==True:
    s1=s
    s=input("Inserisci una stringa:")
    iniziale=s[0]
    if finale==iniziale:
        c=False
        s2=s
    else:
        finale=s[len(s)-1]
print(s1,s2)
