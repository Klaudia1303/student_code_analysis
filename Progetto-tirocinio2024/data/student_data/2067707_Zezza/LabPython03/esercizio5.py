s=input('inserisci stringa: ')
while s.islower()==False or s.isalpha==False:
    print(s[0]+s[-1])
    s=input('inserisci stringa: ')
    if s.islower()==True or s.isalpha==True:
        print(s[0]+s[-1])
