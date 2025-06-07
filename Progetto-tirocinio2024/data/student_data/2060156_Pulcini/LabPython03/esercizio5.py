finito=False
while not finito:
    s=input('stringa s:')
    if s.isalpha()==True and s.islower()==True:
        print(s[0]+s[-1])
        finito=True
    else:
        print(s[0]+s[-1])
        finito=False
