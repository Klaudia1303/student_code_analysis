s=input('inserire una stringa: ')
while s.isalpha()==False or s.islower()==False:
    print(s[0]+s[-1])
    s=input('inserire una stringa: ')
print(s[0]+s[-1])
