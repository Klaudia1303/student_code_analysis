corretto=False
while not corretto:
    s=str(input("Inserisci stringa "))
    c=str(input("Inserisci carattere "))
    if s.count(c)<=2:
        corretto=False
    elif s.count(c)>2:
        print(s.count(c))
        corretto=True
