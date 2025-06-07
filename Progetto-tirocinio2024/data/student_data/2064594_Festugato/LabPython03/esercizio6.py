s = input('inserisci una stringa: ')

i = 0
while i>=0:
    
    
    
    if ord(s[i]) >100:
        print('il primocarattere con codice unicode maggiore di 100 é:',s[i])
        i = -2
    if i==len(s):
        print('stringa consumata e carattere non trovato')
        i = -2
    
    
    i += 1
