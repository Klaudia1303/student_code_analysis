i = 1
while i > 0:
    s = input('inserisci una stringa: ')
    if s.isalpha() and s.islower():
        print( s[0]+s[-1])
        i = 0
    else:
        i = 1
    
