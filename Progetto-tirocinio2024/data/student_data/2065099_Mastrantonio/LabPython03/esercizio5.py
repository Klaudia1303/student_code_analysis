end = False
while not end :
    s = input ('Inserisci una stringa di testo :')
    print (s[0]+s[-1])
    if s.isalpha() and s.islower():
        end = True
