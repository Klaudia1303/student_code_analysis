st=False
while(st==False):
    s=input()
    if (s.islower()==True and s.isalpha()==True):
        st=True
    print(s[0]+s[len(s)-1])
