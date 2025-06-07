corretto=False
while not corretto:
    s=input('Inserire stringa: ')
    if s.isalpha()==True and s.islower()==True:
        print(s[0]+s[-1])
        corretto=True
    else:
        print(s[0]+s[-1])
        s=input('Inserire stringa: ')
