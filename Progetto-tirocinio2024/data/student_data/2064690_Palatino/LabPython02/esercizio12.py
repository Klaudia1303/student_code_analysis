t=input('inserisci il valore della temperatura: ')
c=input('inserisci la scala: ')
C=(F-32)/1.8
if c==F:
   if t<=0:
     print('solida')
   elif t>=100:
     print('gassosa')
   else:
     print('liquida')
elif c==C:
    if t<=0:
     print('solida')
    elif t>=100:
      print('gassosa')
    else:
      print('liquida')
else:
    print(' ')
