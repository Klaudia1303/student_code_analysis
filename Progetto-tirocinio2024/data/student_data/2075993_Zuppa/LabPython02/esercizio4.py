s=input('inserire la stringa   ')
if len(s)> 0 and s[0] == s[len(s)-1]:
    print('caratteri iniziale e finale uguali')
elif len(s)> 0:
    print('caratteri iniziale e finale diversi')
