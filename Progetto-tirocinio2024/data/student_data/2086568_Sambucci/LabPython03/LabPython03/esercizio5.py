corretto=False
while not corretto:
    s=input('Inserire una stringa: ')
    if s.isalpha():
        if s.islower():
            print(s[0]+s[-1])
            corretto=True
        else:
            print(s[0]+s[-1])
    else:
        print(s[0]+s[-1])
        
    
