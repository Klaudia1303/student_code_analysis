i=0
x=0
while i!=1:
    while x<1:
        s=str(input('Inserisci una stringa: '))
        x+=1
        while x>=1 and i!=1:
            y=str(input('Inserisci una stringa: '))
            if y[0]==s[-1]:
                print(s,y)
                i+=1
            s=str(input('Inserisci una stringa: '))
            if y[-1]==s[0]:
                print(y,s)
                i+=1