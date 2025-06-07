c=True
while c:
    s=str(input('Stringa '))
    print(s[0]+s[len(s)-1])
    if s.isalpha()==True:
        if s.islower()==True:
            c=False
    

