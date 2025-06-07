s= str(input('Inserire una stringa: '))
while len(s)<=0:
       s= str(input('Inserire una stringa: '))
if ord(s[0])==ord(s[-1]):
    print ('caratteri iniziale e finale uguali')
else:
    print ('caratteri iniziale e finale diversi')
