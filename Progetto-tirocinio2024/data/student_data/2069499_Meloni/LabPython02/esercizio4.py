s=input('Inserisci una stringa non vuota ')
lung=len(s)
primo=s[0]
ultimo=s[lung-1]
if (primo==ultimo):
    print('caratteri iniziale e finale uguali')
else:
    print('caratteri iniziale e finale diversi')
