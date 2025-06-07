ac=0
i=0
counter=0
continua=True
while continua==True:
    s=str(input("inserisci una stringa: "))
    counter=counter+1
    while len(s)>i:
        if s[i]=='a':
            ac=ac+1
        elif s[i]=='c':
            ac=ac+1
        if ac==2:
            continua=False
        i=i+1
print(counter)
