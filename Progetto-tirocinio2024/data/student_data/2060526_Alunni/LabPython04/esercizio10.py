x = str(input('inserisci una stringa: '))
y = str(input('inserisci una sstringa: '))
z=str(input('inserisci una stringa: '))
X=int(len(x))
Y=int(len(y))
Z=int(len(z))
if X+Y==Z:
    print(x,y,z)
if X+Y!=Z:
    while X+Y!=Z:
        x=y
        y=z
        X=int(len(x))
        Y=int(len(y))
        z=str(input('inserisci una stringa: '))
        Z=int(len(z))
        if X+Y==Z:
            print(x,y,z)
