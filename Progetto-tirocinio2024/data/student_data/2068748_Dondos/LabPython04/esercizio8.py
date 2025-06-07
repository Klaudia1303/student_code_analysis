same = False
prec = input('Inserisci una stringa: ')
last_char = prec[len(prec)-1]

while not same:
    s = input('Inserisci una stringa: ')
    if s[0] == last_char:
        print(prec, s)
        same = True
    else:
        prec = s
        last_char = s[len(s)-1]
        
