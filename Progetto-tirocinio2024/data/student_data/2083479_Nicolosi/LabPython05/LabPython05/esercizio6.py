s=input('Inserisci una stringa: ')
i=0
corretto=True
while i<len(s) and corretto:
    x=s.find(s[i])
    y=s.rfind(s[i])
    if x!=y:
        print(y-x)
        corretto=False
    i+=1