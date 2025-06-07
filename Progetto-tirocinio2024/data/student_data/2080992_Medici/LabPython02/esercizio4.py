s=input('Inserire la stringa: ')
if len(s)==0:
  print('riavviare ed inserire una stringa non vuota')
else:
   i=s[0:1]
   f=s[len(s)-1:len(s)]
   ii=ord(i)
   ff=ord(f)
   if ii==ff:
      print('caratteri iniziale e finale uguali')
   else:
      print('caratteri iniziale e finale diversi')
