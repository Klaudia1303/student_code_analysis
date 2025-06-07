s=''
while s.isalpha()==False or s.islower()==False:
    s=input('inserire una stringa: ')
    l=len(s)
    print(s[0:1],s[(l-1):l])
