a=True
while a:
    s=str(input('scrivi una frase o parola '))
    if s.isalpha()==True and s.islower()==True:
        print(s[0],s[len(s)-1])
        a=False
    else:
        print(s[0],s[len(s)-1])
            
