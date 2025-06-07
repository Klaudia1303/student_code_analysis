s=input('inserire una stringa: ')
stop=False
while not stop:
    if(s.islower(s)==True):
        print(s[0],s[-1])
        stop=True 
    else:
        s=input('inserire una stringa: ')

        
