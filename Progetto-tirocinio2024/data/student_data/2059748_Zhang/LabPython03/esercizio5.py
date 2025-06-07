x=True
while x:
    s=input("una parola a scelta: ")
    if s.isalpha()==True and s.islower()==True:
        print(s[0],s[len(s)-1])
        x=False
    else:
        print(s[0],s[len(s)-1])
