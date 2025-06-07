corretto=False
c=input('Inserire un carattere c: ')
while not corretto:
    s=input('Inserire una stringa: ')
    if s.count(c)>2:
        print(s.count(c))
        corretto=True
