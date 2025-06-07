c = input ('Inserisci un carattere :')
cond = True
while cond == True:
    s = input ('Inserisci una stringa di testo :')
    if s.count(c) >2:
        print (s.count(c))
        cond = False
    else :
        cond = True
