c= True
while c==True:
    s= input('inserire una stringa: ')
    if s.isalpha()==True and s.islower()==True:
        print(str(s[0])+str(s[len(s)-1]))
        c= False
    else:
        print(str(s[0])+str(s[len(s)-1]))
