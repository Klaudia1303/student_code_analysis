i=True
while i==True:
    s=input('inserisci stringa: ')
    if s.isalpha()==True and s.islower()==True:
        print(s[0]+s[-1])
        i=False
    else:
        print(s[0]+s[-1])
