c=input('inserisci un carattere')
finito=False
while not finito:
    s=input('inserisci una stringa: ')
    if s.count(c)>2:
        print(s.count(c))
        finito=True