w = True
while w == True:
    s = str(input('Inserisci una stringa: '))
    print(s[0]+s[-1])
    if s.lower()==s and s.isalpha() == True:
        w = False
