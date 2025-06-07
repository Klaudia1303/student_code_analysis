s='cane3'
while (s.islower()!=True) or (s.isalpha()!=True):
    s=input('Inserire una stringa: ')
    print(s[0]+s[-1])
