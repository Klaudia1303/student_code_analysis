c=input("inserisci un carattere")
corretto=False
while not corretto:
    r=input("inserisci una stringa")
    if r.count(c)>2:
        print(r.count(c))
        corretto=True
    
    
