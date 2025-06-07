finito=False
while not finito:
    s=input('inserire stringa')
    if s.islower():
        print(str(s[0])+str(s[-1]))
        finito=True
    else:
        print(str(s[0])+str(s[-1]))
