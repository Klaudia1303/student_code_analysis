corretto=False
c=input('inserisci un carattere')
while not corretto:
    s=input('inserisci sequenza di stringhe')
    if s.count(c)>2:
        print(s.count(c))
        corretto:True
