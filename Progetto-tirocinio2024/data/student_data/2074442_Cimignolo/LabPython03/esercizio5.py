boo=True

while boo:
    s=input('inserisci una stringa: ')
    print(s[0]+s[-1])
    if s.isalpha() and s.islower():
        boo=False
    
