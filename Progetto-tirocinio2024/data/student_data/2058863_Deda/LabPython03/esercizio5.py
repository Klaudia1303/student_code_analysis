corretto=False
while not corretto:
    s=str(input("Inserisci stringa "))
    if (s.isalpha()==False) or (s.islower()==False):
        print(s[0]+s[-1])
        corretto=False
    elif (s.isalpha()==True) and (s.islower()==True):
        print(s[0]+s[-1])
        corretto=True
