s=input('inserici una stringa: ')
a=len(s)
if a>0:
    if s[0]==s[a-1]:
        print('caratteri iniziale e finale uguali')
    else:
        print('caratteri iniziale e finale divesi')
else:
    print('la stringa è vuota')
