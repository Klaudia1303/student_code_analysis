s=str(input('Inserisci stringa '))
differenza=0
for i in range(len(s)):
    x=s[i]
    y=s.find(x)
    z=s.rfind(x)
    provvisoria=z-y
    if provvisoria>differenza:
        differenza=provvisoria
print(differenza)
