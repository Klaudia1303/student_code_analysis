i=0
while i!=1:
    s=input('inserire una stringa: ')
    s1=len(s)
    if s.isalpha()==True and s.islower()==True:
        print(str(s[0]+s[s1-1]))
        i=1
    else:
         print(str(s[0]+s[s1-1]))
    
    
          

    
