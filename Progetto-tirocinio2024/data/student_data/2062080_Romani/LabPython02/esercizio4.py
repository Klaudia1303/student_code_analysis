s=input('Inserire stringa: ')
primo=int(0)
ultimo=int(len(s)-1)
if s[primo]==s[ultimo]:
    print('caratteri iniziale e finale uguali')
else:
    print('caratteri iniziale e finale diversi')
