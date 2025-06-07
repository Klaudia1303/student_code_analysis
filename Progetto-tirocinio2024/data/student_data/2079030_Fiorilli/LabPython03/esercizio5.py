s='1a0'
while not (s.isalpha() and s.islower()):
    s=input('inserisci una stringa: ')
    print (s[0]+s[len(s)-1])
    
