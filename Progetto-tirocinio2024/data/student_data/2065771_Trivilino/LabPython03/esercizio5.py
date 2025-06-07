s='1A'
while s.isalpha()==False or s.islower()==False:
    s=input('Inserire una stringa: ')
    print (s[0:1]+s[-1:])
