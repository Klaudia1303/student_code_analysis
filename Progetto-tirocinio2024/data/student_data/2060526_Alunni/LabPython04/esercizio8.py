x = str(input('inserisci una stringa: '))
y = str(input('inserisci una sstringa: '))
if x!='' and y!='':
    X=x[-1]
    Y=y[0]
    if X==Y:
        print(x,y)
    while X!=Y :
        if x!='' and y!='':
            x=y
            y = str(input('inserisci una stringa: '))
            X=x[-1]
            Y =y[0]
    if X==Y:
        print(x,y)
