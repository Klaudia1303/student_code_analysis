s=input('Inserisci una stringa: ')
if s.isalpha()==True and s.islower()==True:
    print(s[0]+s[-1])
else:
    while not (s.isalpha()==True and s.islower()==True):
        print(s[0]+s[-1])
        s=input('Inserisci una stringa: ')
    if s.isalpha()==True and s.islower()==True:
        print(s[0]+s[-1])