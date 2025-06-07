s=str(input())
if len(s)==0:
    print('Stringa vuota')
else:
    if s[0]==s[len(s)-1]:
        print('Caratteri iniziale e finale uguali')
    else:
        print('Caratteri iniziale e finale diversi')
